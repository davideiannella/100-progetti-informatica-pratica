import socket
import threading

def tcp_roundtrip(payload=b"hello"):
    if not isinstance(payload, bytes) or len(payload) > 1024 * 1024:
        raise ValueError("payload bytes fino a 1 MiB")
    errors = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.bind(("127.0.0.1", 0))
        listener.listen(1)
        listener.settimeout(3)

        def server():
            try:
                conn, _ = listener.accept()
                with conn:
                    conn.settimeout(3)
                    chunks = []
                    while True:
                        chunk = conn.recv(4096)
                        if not chunk:
                            break
                        chunks.append(chunk)
                    conn.sendall(b"".join(chunks))
            except Exception as exc:
                errors.append(exc)

        worker = threading.Thread(target=server, daemon=True)
        worker.start()
        try:
            with socket.create_connection(listener.getsockname(), timeout=3) as client:
                client.sendall(payload)
                client.shutdown(socket.SHUT_WR)
                chunks = []
                while True:
                    chunk = client.recv(4096)
                    if not chunk:
                        break
                    chunks.append(chunk)
        finally:
            worker.join(4)
        if worker.is_alive():
            raise TimeoutError("server ancora attivo")
        if errors:
            raise errors[0]
        return b"".join(chunks)

def udp_roundtrip(payload=b"hello"):
    if not isinstance(payload, bytes) or len(payload) > 65507:
        raise ValueError("payload UDP IPv4 troppo grande")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
        server.bind(("127.0.0.1", 0))
        server.settimeout(3)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
            client.settimeout(3)
            client.sendto(payload, server.getsockname())
            data, addr = server.recvfrom(65535)
            server.sendto(data, addr)
            return client.recvfrom(65535)[0]

def simulated_udp_delivery(packets, drop_every=3):
    if type(drop_every) is not int or drop_every <= 0:
        raise ValueError("drop_every intero positivo")
    return [p for i, p in enumerate(packets, 1) if i % drop_every != 0]
