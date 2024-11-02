import scapy.all as scapy


def packet_handler(packet):
    if packet[scapy.IP].ttl == 1:
        packet.show()
        exit()


if __name__ == "__main__":
    scapy.sniff(filter="icmp", prn=packet_handler)
