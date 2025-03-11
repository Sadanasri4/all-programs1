from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

# Callback function to process packets
def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        print(f"IP Packet: {ip_src} -> {ip_dst} (Protocol: {proto})")

        if TCP in packet:
            print(f"TCP Segment: {packet[TCP].sport} -> {packet[TCP].dport}")
        elif UDP in packet:
            print(f"UDP Datagram: {packet[UDP].sport} -> {packet[UDP].dport}")

# Start packet sniffing (you can specify a network interface if needed)
print("Starting packet capture...")
sniff(prn=packet_callback, filter="ip", store=0)
