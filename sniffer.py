from scapy.all import *

def sniff_packets(packet):
    if packet.haslayer(Raw):
        payload = packet[Raw].load
        if b"HTTP" in payload:
            print(payload)

sniff(filter="tcp port 80", prn=sniff_packets)