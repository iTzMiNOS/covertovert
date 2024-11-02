import scapy.all as scapy


if __name__ == '__main__':
    packet = scapy.IP(dst='receiver', ttl=1) / scapy.ICMP()
    scapy.send(packet)
