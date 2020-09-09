import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 65535


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)

data = conn.recv(1024)
print ("received data:", data)
conn.close()
