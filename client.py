import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "Time"

sock.sendto(msg.encode(), ('localhost', 1234))

data,addr= sock.recvfrom(4096)
data = str(data, "utf-8")
print(data)
