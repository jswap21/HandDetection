import cv2


cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    cv2.imshow("Media Controller", image)
    # Quit the window on pressing Sapcebar key
    key = cv2.waitKey(1)
    if key == 32:
        break
    