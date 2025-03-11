import nmap

def scan_ports(target, port_range='1-1024'):
    # Initialize the nmap PortScanner object
    nm = nmap.PortScanner()
    
    # Perform the scan on the target within the specified port range
    nm.scan(target, port_range)
    
    # Collect and print the results
    for host in nm.all_hosts():
        print(f'Host : {host} ({nm[host].hostname()})')
        print(f'State : {nm[host].state()}')
        
        for proto in nm[host].all_protocols():
            print(f'Protocol : {proto}')
            ports = nm[host][proto].keys()
            
            for port in ports:
                print(f'Port : {port}\tState : {nm[host][proto][port]["state"]}')

if __name__ == '__main__':
    target = input("Enter the target (IP or domain): ")
    port_range = input("Enter the port range (e.g., 1-1024): ")
    
    if not port_range:
        port_range = '1-1024'  # Default port range if not provided
    
    scan_ports(target, port_range)
