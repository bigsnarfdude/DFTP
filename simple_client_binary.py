import socket
import time
import sys
import binascii
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 5555
MESSAGE = (1, 'ab', 2.2)
packer = struct.Struct("I 2s f")
packed_data = packer.pack(*MESSAGE)

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE
print "binary:", packed_data

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(packed_data, (UDP_IP, UDP_PORT))
time.sleep(2)


