import pywhatkit as kit

print("🤖 Welcome..! 🤖")
phone_number = input("Phone Number : ")
msg = input("Write msg: ")

print("\nTime")
hour = int(input("Hour: "))
minute = int(input("Minute: "))

print(f"\n🚀 Done!..!" )

kit.sendwhatmsg(phone_number, msg, hour, minute)

