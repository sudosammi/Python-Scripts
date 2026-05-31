import qrcode

data = input("Enter link to generate QR Code : ")


file_name = input("Enter file name : ")
if file_name == "":
    file_name = "qr_code.png"
else:
    if not file_name.endswith(".png"):
        file_name += ".png"


print("QR Code Generating")

qr_img = qrcode.make(data)

qr_img.save("qr_code.png")

print(f"QR save as qr_code,png" )

