import qrcode
import os


qr_str = "Hi This is Azeemushan Ali"
img = qrcode.make(qr_str) #Generates the QR Code
img.save('qr.png',"PNG") # Save as a image

os.startfile('qr.png') # Opens the Image
