#TCP CLIENT

from scapy.all import *

def send_data(target_ip, target_port, message):
    #Setting Variables
    target_ip = str(input("[+] Input the Target Ip:   "))
    target_port = str(input("[+] Input the Target Port:  "))
    # Create an IP layer and a TCP layer
    ip = IP(dst=target_ip)
    tcp = TCP(dport=target_port, flags="S")  # SYN packet to start the handshake
    
    # Send SYN packet to initiate the connection
    syn_ack = sr1(ip/tcp, timeout=1)
    
    # Create the ACK packet (part of the 3-way handshake)
    ack = TCP(dport=target_port, flags="A", seq=syn_ack.ack, ack=syn_ack.seq + 1)
    send(ip/ack, verbose=0)
    
    # Now send the actual data (sending the message)
    tcp_data = TCP(dport=target_port, flags="A", seq=syn_ack.ack, ack=syn_ack.seq + 1)
    payload = Raw(load=message)
    
    # Send data
    send(ip/tcp_data/payload, verbose=0)
    print(f"Message sent to {target_ip}:{target_port}: {message}")

# Example usage
send_data("192.168.1.100", 4444, "Hello from Scapy Netcat!")
