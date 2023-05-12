import ipaddress

def cidr_info(cidr):
    network = ipaddress.ip_network(cidr, strict=False)
    netmask = network.netmask
    first_ip = network.network_address + 1
    last_ip = network.broadcast_address - 1
    total_hosts = network.num_addresses - 2 # subtract network and broadcast addresses
    return str(netmask), str(first_ip), str(last_ip), total_hosts

cidr = input("Enter CIDR: ")
netmask, first_ip, last_ip, total_hosts = cidr_info(cidr)

print(f"Netmask: {netmask}")
print(f"First IP: {first_ip}")
print(f"Last IP: {last_ip}")
print(f"Total Hosts: {total_hosts}")