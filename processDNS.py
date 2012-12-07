#! /usr/bin/env python
'''
processes DNS packets outputed by tcpdump into dataset for sklearn
'''

INPUTFILE = '/Users/antigen/dev/DFTP/dataDNS'
OUTPUTFILE = '/Users/antigen/dev/DFTP/dataDNS.csv'


def process_DNS_answers(data):
    for line in data:
        if "A?" not in line:
            print line #data is all over the place

def process_time(packet):
    time_stamp = packet[0].split(':')
    time_stamp.pop()
    return "".join(time_stamp)

def process_ip(packet): 
    ip_address = packet[2].split('.')[0:-1]
    return ".".join(ip_address)

def process_port(packet):
    return int(packet[2].split('.')[-1])

def process_tld(packet):
    pass # use tld package 
    # https://github.com/john-kurkowski/tldextract

def process_destination_port(packet):
    port = packet[5]
    if "+" in port:
        port = port[:-1]
        return int(port)
    else:
        return int(port)

def process_record_type(packet):
    return packet[6]

def process_DNS_payload(packet):
    return packet[7][:-1]

def process_length(packet):
    return int(packet[8].strip(")("))

def process_packet(line):
    return process_time(line),process_ip(line),process_destination_port(line),process_record_type(line),process_DNS_payload(line),process_length(line)

def process_DNS_requests(data):
    for line in data:
        packet = line.split()
        if "A?" in packet:
            print process_packet(packet)

data = open(INPUTFILE).readlines()
process_DNS_requests(data)
