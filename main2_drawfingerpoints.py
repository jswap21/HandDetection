import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

# Define a function to 
def drawHandLanmarks(image, hand_landmarks):
    print(hand_landmarks)
    # Draw connections between landmark points
    if hand_landmarks:

      for landmarks in hand_landmarks:
               
        mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)



while True:
    success, image = cap.read()
    output=hands.process(image)
    landmarks=output.multi_hand_landmarks
    drawHandLanmarks(image,landmarks)
    cv2.imshow("Media Controller", image)
    # Quit the window on pressing Sapcebar key
    key = cv2.waitKey(1)
    if key == 32:
        break
    