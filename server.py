import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

conn = ('10.128.0.3', 1234)

sock.bind(conn)
print("UDP Socket Running")

while True:
    data, addr = sock.recvfrom(4096)
    data = str(data, "utf-8")
    print(f"Data :{data}")
    print(f"Address :{addr}")
    resp = time.ctime()
    resp = resp.encode()
    sock.sendto(resp, addr)
