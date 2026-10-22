from pathlib import Path
import sys,socket,threading,json,hashlib,struct
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from file_transfer import *
def exchange(data):
    a,b=socket.socketpair();a.settimeout(3);b.settimeout(3)
    errors=[]
    def sender():
        try:
            with a: send_file(a,'binary.bin',data)
        except Exception as e: errors.append(e)
    t=threading.Thread(target=sender);t.start()
    try:
        with b: result=receive_file(b)
    finally:t.join(4)
    assert not errors and not t.is_alive()
    assert result==('binary.bin',data)
for data in [b'',bytes(range(256))*2048]: exchange(data)
# Ogni byte del frame arriva separatamente.
a,b=socket.socketpair();a.settimeout(3);b.settimeout(3)
packet=struct.pack('!I',7)+b'abcdefg'
def fragment():
    with a:
        for byte in packet:a.sendall(bytes([byte]))
t=threading.Thread(target=fragment);t.start()
with b: assert recv_frame(b)==b'abcdefg'
t.join(4)
for meta,data in [({'name':'../x','size':0,'sha256':hashlib.sha256(b'').hexdigest()},b''),
                  ({'name':'x','size':3,'sha256':'0'*64},b'bad'),
                  ({'name':'x','size':True,'sha256':'0'*64},b'')]:
    a,b=socket.socketpair()
    with a,b:
        send_frame(a,json.dumps(meta).encode());send_frame(a,data)
        try:receive_file(b)
        except ValueError:pass
        else:raise AssertionError('bad metadata accepted')
a,b=socket.socketpair()
with a,b:
    a.sendall(struct.pack('!I',MAX_FILE+1))
    try:recv_frame(b)
    except ValueError:pass
    else:raise AssertionError('oversized header')
a,b=socket.socketpair()
with a,b:
    a.sendall(struct.pack('!I',5)+b'xx');a.shutdown(socket.SHUT_WR)
    try:recv_frame(b)
    except ConnectionError:pass
    else:raise AssertionError('truncated stream')
print('P049 PASS: frame frammentati, 512 KiB, hash, path, EOF e limiti')
