import subprocess


print("Welcome to my macchanger script!")

def change_mac(interface, new_mac):
    print(f"\n[+] Changing Mac address for {interface} to {new_mac}...")
 
    # close wifi
    subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "down"])

     #set new <MAC
    subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "address", new_mac]) 
    

     # open wifi
    subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "up"])
  
    print("\n Boom! MAC address successfully changed")


#inputs

iface = input("Interface name : ")
new_m = input("New MAC address : ")

change_mac(iface, new_m)