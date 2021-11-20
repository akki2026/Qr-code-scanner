import cv2

# initalize the camera
cap = cv2.VideoCapture(0)
# initialize the OpenCV QRCode detector
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()

    data, vertices_array, _ = detector.detectAndDecode(img)

    if vertices_array is not None:
        if data:
            print("QR Code detected, data:", data)

    # display the result
    cv2.imshow("QrCodeDecoder", img)

    if cv2.waitKey(1) == ord("e"):
        break
cap.release()
cv2.destroyAllWindows()