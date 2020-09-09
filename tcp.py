import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 65535
BUFFER_SIZE = 1024


MESSAGE = b"Hello, World! So here we are again and I Just wanted to say hello to everyone!!!! Woot Woot"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
