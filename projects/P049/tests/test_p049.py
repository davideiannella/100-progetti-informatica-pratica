import sys,pathlib,socket,threading
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from file_transfer import send_file, receive_file

a,b=socket.socketpair()
payload=(b"reti-e-sistemi-"*1000)
out={}
t=threading.Thread(target=lambda: send_file(a,"manuale.bin",payload))
t.start()
name,data=receive_file(b)
t.join()
a.close(); b.close()
assert name=="manuale.bin" and data==payload

bad=False
try:
    x,y=socket.socketpair()
    send_file(x,"../secret.txt",b"x")
except ValueError:
    bad=True
finally:
    x.close(); y.close()
assert bad
print("P049: framed transfer + SHA-256 PASS")
