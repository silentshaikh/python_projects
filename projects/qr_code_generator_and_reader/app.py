# import qrcode

# data = "Be a Batman"
# qrImg= qrcode.make(data)

# qrImg.save("C:/Users/hp/Desktop/python_assignment/projects/qr_code_generator_and_reader/codeData2.png")

# qrcode reader

import cv2


imgFile = cv2.imread("C:/Users/hp/Desktop/python_assignment/projects/qr_code_generator_and_reader/codeData2.png")


codeDetector = cv2.QRCodeDetector()
# showQrCodeData = decode(imgFile)
qrData, bBox, straightQrCode = codeDetector.detectAndDecode(imgFile)
# print(showQrCodeData)

if qrData:
    print(qrData)
else:
    print("QR Code not Found")