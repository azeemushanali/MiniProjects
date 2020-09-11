import cv2
import numpy as np
import sys
import time

img_path = './qr.png'
inputImage = cv2.imread(img_path)

# Display barcode and QR code location
def display(im, bbox, data):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)
        cv2.putText(im,data, (15,20),
            2, 0.65, (255,0,0), 1)

    # Display results
    cv2.imshow("Results", im)

# Create a qrCodeDetector Object
qrDecoder = cv2.QRCodeDetector()

# Detect and decode the qrcode
t = time.time()
data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
print("Time Taken for Detect and Decode : {:.3f} seconds".format(time.time() - t))
if len(data)>0:
    print("Decoded Data : {}".format(data))
    display(inputImage, bbox, data)
    rectifiedImage = np.uint8(rectifiedImage);
    #cv2.imshow("Rectified QRCode", rectifiedImage);
else:
    print("QR Code not detected")
    cv2.imshow("Results", inputImage)
cv2.imwrite("output.jpg",inputImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
