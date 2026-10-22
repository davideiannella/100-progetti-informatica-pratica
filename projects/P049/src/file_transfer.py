import hashlib
import json
import struct

HEADER = struct.Struct("!I")
MAX_FILE = 8 * 1024 * 1024
MAX_META = 4096

def safe_name(name):
    if (not isinstance(name, str) or name in {"", ".", ".."}
            or any(c in name for c in ("/", "\\", "\0", ":"))):
        raise ValueError("nome file non sicuro")
    return name

def send_frame(sock, payload: bytes):
    if not isinstance(payload, bytes) or len(payload) > MAX_FILE:
        raise ValueError("frame troppo grande o non bytes")
    sock.sendall(HEADER.pack(len(payload)) + payload)

def recv_exact(sock, n):
    if type(n) is not int or not 0 <= n <= MAX_FILE:
        raise ValueError("dimensione non valida")
    chunks = []
    while n:
        chunk = sock.recv(min(n, 65536))
        if not chunk:
            raise ConnectionError("stream terminato")
        chunks.append(chunk)
        n -= len(chunk)
    return b"".join(chunks)

def recv_frame(sock, limit=MAX_FILE):
    size = HEADER.unpack(recv_exact(sock, HEADER.size))[0]
    if size > limit:
        raise ValueError("frame oltre limite")
    return recv_exact(sock, size)

def send_file(sock, name: str, data: bytes):
    safe_name(name)
    if not isinstance(data, bytes) or len(data) > MAX_FILE:
        raise ValueError("file troppo grande o non bytes")
    meta = {"name": name, "size": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    header = json.dumps(meta).encode()
    if len(header) > MAX_META:
        raise ValueError("metadati troppo grandi")
    send_frame(sock, header)
    send_frame(sock, data)

def receive_file(sock):
    meta = json.loads(recv_frame(sock, MAX_META))
    if not isinstance(meta, dict):
        raise ValueError("metadati non validi")
    name = safe_name(meta.get("name"))
    size = meta.get("size")
    digest = meta.get("sha256")
    if type(size) is not int or not 0 <= size <= MAX_FILE:
        raise ValueError("dimensione non valida")
    if not isinstance(digest, str) or len(digest) != 64:
        raise ValueError("checksum non valido")
    data = recv_frame(sock, size)
    if len(data) != size or hashlib.sha256(data).hexdigest() != digest:
        raise ValueError("dimensione o checksum non coerenti")
    return name, data
