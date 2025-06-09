#Write a script that reads a list of IPs and pings each one.

import os
ipAddresses = [
    "127.0.0.1",       # Localhost (your machine)
    "192.168.1.1",     # Common router IP
    "192.168.1.10",    # Sample host in LAN
    "192.168.1.20",
    "192.168.1.30",
    "10.0.0.1",        # Private Class A
    "10.0.0.2",
    "10.10.10.10",     # Common in HackTheBox
    "172.16.0.1",      # Private Class B
    "172.16.1.1"
]
for ip in ipAddresses:
    print(os.system(f"ping {ip}"))

# Try brute-forcing a login page with a list of usernames and passwords (using requests module).
