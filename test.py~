import socket
import time

HOST = ""
PORT = 5353
DATA = "TEST"

while True:
    udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print "Sending data <%s>" % DATA
    udpSock.sendto(DATA,(HOST,PORT))
    udpSock.close()
    time.sleep(2)
