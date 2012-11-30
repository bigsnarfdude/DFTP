import socket
import time
import hashlib

UDP_IP = "127.0.0.1"
UDP_PORT = 5555
MESSAGE = "This is the secret message. I love DFTP. This is the end of the secret message."
SPLIT_MESSAGE = MESSAGE.split()

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

for word in SPLIT_MESSAGE:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    m = hashlib.sha256()
    m.update(word)
    sock.sendto(m.hexdigest(), (UDP_IP, UDP_PORT))
    time.sleep(0.5)


