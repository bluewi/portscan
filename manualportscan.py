import socket

def scan_ports(domain, port_range):
    open_ports = []
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((domain, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

domain = 'google.com'
port_range = range(1, 443)  # Scanning ports 1 to 1024

open_ports = scan_ports(domain, port_range)
print(f"Open ports on {domain}: {open_ports}")
