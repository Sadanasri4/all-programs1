from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        
        # Determine the protocol (TCP, UDP, etc.)
        if proto == 6:  # TCP
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif proto == 17:  # UDP
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        else:
            protocol = "Other"
            src_port = "N/A"
            dst_port = "N/A"
        
        print(f"Protocol: {protocol} | Source: {ip_src}:{src_port} | Destination: {ip_dst}:{dst_port}")
        
        # Print payload data if available
        if Raw in packet:
            print(f"Payload: {packet[Raw].load}\n")

def main():
    print("Starting Packet Sniffer...")
    # Sniffing packets on all interfaces (interface="eth0" for specific interface)
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
