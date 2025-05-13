import qrcode
from PIL import Image

qr=qrcode.QRCode(version=None,
                 error_correction=qrcode.constants.ERROR_CORRECT_L,
                 box_size=10,border=4)
#   input URL
url = input("Enter the URL to generate a QR code: ")
qr.add_data(url)
qr.make(fit=True)
img=qr.make_image(fill_Color="green",back_color="black")
png=".png"
fillname=input(f"QR-Code save as : ")+png
img.save(png)