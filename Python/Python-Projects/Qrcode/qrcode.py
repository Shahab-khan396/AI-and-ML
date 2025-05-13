import qrcode as qr

#   input URL
url = input("Enter the URL to generate a QR code: ")

# Create a QR code object with the provided URL
img = qr.make(url)

# Save the QR code image with a descriptive name
png=".png"
filename = input("image save as :")+png
img.save(filename)

print(f"QR code generated and saved as '{filename}'.")
