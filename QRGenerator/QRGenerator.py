# Importing QR Code Module ! Please install before importing using python pip install qrcode
import qrcode 
from PIL import Image
import qrcode.constants 

qr = qrcode.QRCode(version=1, 
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=25, border=4)

# Here we will add the websites.. You can edit it to anything you want.
qr.add_data("https://www.google.co.in")
qr.make(fit=True)
# You can change the color to anything you want
img = qr.make_image(fill_color = "Black", back_color = "white")
img.save("Generated QR.png")
