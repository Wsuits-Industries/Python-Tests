print("""
((WSUITS PORT SCANNER))
wsuits@gmail.com
""")
from scapy.all import *

target = input("[+] Input Target IP Address: ")
ports = [21, 22, 80, 443, 8080, 53, 5500, 6606, 25, 445, 300, 100]

for port in ports:

    #crafting packet to send to specified ports packet contians the TCP SYN flag
    pkt = IP(dst=target)/TCP(dport=port, flags="S")

    #reading response Using a vaiable resp
    resp = sr1(pkt, timeout=1, verbose=3)

    #checking if the resp has a tcp layer 
    if resp and resp.haslayer(TCP):

        if resp.getlayer(TCP).flags == 0x12:
            hexdump(resp)
            print(f"[+] Port {port} is open")

        elif resp.getlayer(TCP).flags == 0x14:
            hexdump(resp)
            print(f"[-] Port {port} is closed")
        
    