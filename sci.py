# Import everything from scapy
from scapy.all import *

# Ask the user to enter the target IP address
target_ip = input("[+] What is the Target IP Address: ")

# Create a packet
packet = Ether()/IP(src=target_ip, dst=target_ip, ttl=10)/TCP(dport = 80, )/ICMP()

# Print the source IP address of the packet
print(f"[+] The Source IP Address is: {packet.src}")

# Inform the user about IP hiding (this script does not hide IP by default)
print("[-] Note: This script does NOT hide your IP address.")


# 'send' function sends the packet at Layer 3 (IP Layer)
sr(packet)

# Print the destination IP address to confirm where the packet is sent
print(f"[+] Packet sent to Destination IP: {packet.dst}")

# Ask the user if they want to see a hexdump of the packet bytes
hexdump_choice = input("[+] Do you want a hexdump of the packet? (Y/N): ")

# If the user chooses 'Y', show the packet's hex representation and raw bytes
if hexdump_choice.upper() == "Y":
    # Show packet in hexadecimal and ASCII format
    hexdump(packet)
    # Print the raw bytes of the packet
    print(raw(packet))
