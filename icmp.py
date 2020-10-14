from socket import *
import socket
import os
import sys
import struct
import time
import select
import binascii

level = 0
code = 0
identify = 0
sequence = 0
address = '192.168.1.1'

def checksum(source_string):
    countTo = (int(len(source_string)/2))*2
    sum = 0
    count = 0

    loByte = 0
    hiByte = 0
    while count < countTo:
        if (sys.byteorder == "little"):
            loByte = source_string[count]
            hiByte = source_string[count + 1]
        else:
            loByte = source_string[count + 1]
            hiByte = source_string[count]
        try:     # For Python3
            sum = sum + (hiByte * 256 + loByte)
        except:  # For Python2
            sum = sum + (ord(hiByte) * 256 + ord(loByte))
        count += 2


    if countTo < len(source_string): # Check for odd length
        loByte = source_string[len(source_string)-1]
        sum += loByte

    sum &= 0xffffffff

    sum = (sum >> 16) + (sum & 0xffff)
    sum += (sum >> 16)
    answer = ~sum & 0xffff
    answer = htons(answer)

    return answer



s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

icmp = struct.pack(">BBHHH", level, code, 0, identify, sequence)
chksum=checksum (icmp)

sendme = struct.pack(">BBHHH", level, code, chksum, identify, sequence)




print ("In Progress")
for i in range(300):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    icmp = struct.pack(">BBHHH", level, code, 0, identify, sequence)
    chksum=checksum (icmp)

    sendme = struct.pack(">BBHHH", level, code, chksum, identify, sequence)
    s.sendto(sendme, (address, 0))
    code = code + 1
    if code > 6:
        code = 0
        level = level + 1
    if level > 20:
        level = 0
    sequence = sequence + 11
    identify = identify + 13


    time.sleep(.5)

print ("Complete")
