import socket
import time


def udpsocket1(msg):
	UDP_IP = "192.168.22.23"
	UDP_PORT = 20
	sock.sendto(msg, (UDP_IP, UDP_PORT))
def udpsocket2(msg):
	UDP_IP = "192.168.33.23"
	UDP_PORT = 20
	sock.sendto(msg, (UDP_IP, UDP_PORT))

Message = "Oh Wee Here we go!!!!!"
translate1 = Message.encode()

Message = "What did I write Here"
translate2 = Message.encode()



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 2000))
print ("In Progress")
for i in range(3):
    udpsocket1(translate1)
    udpsocket2(translate2)


    time.sleep(.5)

print ("Complete")
