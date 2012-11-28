import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

udp_service = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_service.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = udp_service.recvfrom(1024)
    print "received message:", data
