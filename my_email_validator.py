import re

print("📧 Email Validator Script")
print(" For End type quit. \n")

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

while True:
    user_email = input("For Check Enter Email : ")
    
    if user_email.lower() == "quit":
        print("Script closing ")
        break

  
    if re.search(pattern, user_email):
        print("✅ VALID!\n")
    else:
        print("❌ FAKE/INVALID!\n")
