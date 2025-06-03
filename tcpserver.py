#TCP SERVER

from scapy.all import *

def listen_for_data(local_ip, local_port):
    #setting Sever Ip address Port number
    # local_ip = input("[+] what is the Port number of your server: ")
    # local_port = input("[+] what is the specified port number ")
    # Create an IP layer and a TCP layer with the SYN-ACK flag set
    ip = IP(dst=local_ip)
    tcp = TCP(dport=local_port, flags="S")
    
    # Wait for an incoming connection (SYN packet)
    syn_ack = sr1(ip/tcp, timeout=1)
    
    # Send the ACK packet (completing the 3-way handshake)
    ack = TCP(dport=local_port, flags="A", seq=syn_ack.ack, ack=syn_ack.seq + 1)
    send(ip/ack, verbose=0)
    
    # Listen for data sent by the client
    while True:
        packet = sniff(filter=f"tcp and port {local_port}", count=1, timeout=10)
        if packet:
            # If the packet contains data (TCP + Raw payload)
            if Raw in packet:
                print(f"Received message: {packet[Raw].load.decode()}")
        else:
            print("No data received.")

# Example usage
listen_for_data("0.0.0.0", 4444)
