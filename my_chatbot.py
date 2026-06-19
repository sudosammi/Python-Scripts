import socket
import threading
import sys

print("🕵️‍♂️ Welcome to Anonymous Terminal Chatbox 🕵️‍♂️")
print("-" * 45)

# Socket setup (UDP protocol use for chat)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Details mangna
my_ip = input("Enter IP : ")
my_port = int(input("Port : "))

target_ip = input("\nTarget IP : ")
target_port = int(input("Target Port : "))

# ......
s.bind((my_ip, my_port))

print(f"\n[+] Chatbox Active! You Listen {my_port}.")
print("[+] Message type and press Enter. (For close type 'quit')\n")

# message receive function
def receive_msg():
    while True:
        try:
            msg = s.recvfrom(1024)
            # new msg print terminal 
            print(f"\n[Target Hacker]: {msg[0].decode()}")
        except:
            pass

# Threading magic - Receive in  background thread 
t = threading.Thread(target=receive_msg)
t.daemon = True
t.start()

# Message send wala loop
while True:
    my_msg = input("")
    if my_msg.lower() == "quit":
        print("Chatbox Closing...")
        sys.exit()
    
    # Message send
    s.sendto(my_msg.encode(), (target_ip, target_port))
