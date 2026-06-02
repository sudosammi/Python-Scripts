import scapy.all as scapy

print("Network Scanning.......\n")

def scan(ip):

    arp_request = scapy.ARP(pdst=ip)

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast / arp_request

    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP Address\t\tMac Address")
    print("__")
    print("--------")
    print("---------------------------------")

    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)

target_ip = input("IP Address : ")

if target_ip == "":
    target_ip = "192.168.1.1/24"  #Default

scan(target_ip)
