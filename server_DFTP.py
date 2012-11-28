#! /usr/bin/env python
'''
This progam is the server portion of DFTP and it is the destination and storage of the exfiltrated data from a host using the DFTP client progam. The server looks and acts like a DNS server. Packets are UDP and look like DNS packets except for payload. This program is built to test DFIR response teams and DFIR tools.
'''

import socket
HOST = ""
PORT = 53


class Server:
    def __init__():
        pass

    def start(HOST, PORT):
        udp_service = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_service.bind((HOST, PORT))

    def buffer():
        data, addr = udp_service.recvfrom(1024)

    def decode_message_identifier(data):
        pass

    def decrypt_message_payload(data):
        pass

    def store_decrypted_ojbect(data):
        pass

    def message_text_reassembler(data):
        text_message.append(data)
        print "Data %s added to text_message" % data
    
    def get_message_text():
        print "Here is the exfiltrated data so far"
        time.sleep(1)
        print text_message

    def message_picture_reassembler(data):
        pass

    def message_music_reassembler(data):
        pass

    def message_file_reassembler(data):
        pass

    def message_pdf_reassembler(data):
        pass

    def message_excel_reassembler(data):
        pass

    def message_doc_reassembler(data):
        pass



