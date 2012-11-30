import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5555

udp_service = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_service.bind((UDP_IP, UDP_PORT))

text_message = []

def message_text_reassembler(data):
    text_message.append(data)

while True:
    data, addr = udp_service.recvfrom(1024)
    print "received message:", data.decode('hex')
    #message_text_reassembler(data)
    #print text_message
