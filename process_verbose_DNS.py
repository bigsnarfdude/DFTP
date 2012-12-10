data_example1 = "13:17:45.698317 IP (tos 0x0, ttl 255, id 51439, offset 0, flags [none], proto UDP (17), length 57) lxp-151308.natnast.com.61232 > gc._msdcs.nypl.net.domain: [udp sum ok] 54171+ A? ocw.mit.edu. (29)"

data_example2 = "23:59:07.168532 IP (tos 0x0, ttl 64, id 45399, offset 0, flags [none], proto UDP (17), length 72) 192.168.1.45.55550 > google-public-dns-a.google.com.domain: [udp sum ok] 5824+ AAAA? keyvalueservice.icloud.com. (44)"

data_example3 = "14:13:09.493604 IP (tos 0x0, ttl 64, id 35079, offset 0, flags [none], proto UDP (17), length 97) 10.242.11.216.verismart > google-public-dns-a.google.com.domain: [udp sum ok] 53132+ A? b47f363e2b430c0647f14deea3eced9b0ef300ce.badguy.com. (69)"


'''
tcpdump -i en1 -vv udp dst port 53 > dns_file
'''

data=[]
with open('dns_file') as f:
    for line1 in f:
        line2 = f.next()
        data.append(line1+line2)

tos, ttl, identification, offset, flags, proto, length, src_ip, src_port, dst_ip, dst_port, udp_sum, num1, record_type, dns_reply, num2 = line.spit()


map(function, iterable)

def tos(data):
    line = data.split(',')
    return line[0].split()[-1]

def ttl(data):                                                                                           
    line = data.split(',')
    return line[1].split()[-1]

def identification(data):
    line = data.split(',')
    return line[2].split()[-1]

def offset(data):
    line = data.split(',')
    return line[3].split()[-1]

def flags(data):
    line = data.split(',')
    return line[4].split()[-1].strip('][')

def proto(data):
    line = data.split(',')
    return line[5].split()[1]

def length(data):
    line = data.split(',')
    return line[6].split()[1].strip(')(')

def src_ip(data):
    line = data.split()
    line = line[17].split('.')[:-1]
    return '.'.join(line)

def src_port(data):
    line = data.split()
    return line[17].split('.')[-1]

def dst_ip(data):
    line = data.split()
    return line[18][:-1]

def dst_(data):
    line = data.split()
    return line[19]

def udp_sum(data):
    line =  data.split()
    return line[20].strip(']['), line[21], line[22].strip('][')

def unknown_num(data):
    # line = data.split()
    # return line[23]
    pass

def record_type(data):
    line = data.split()
    return line[24]

def dns_reply(data):
    line = data.split()
    return line[25]

def unknown_num(data):
    line = data.split()
    return line[26].strip(')(')

