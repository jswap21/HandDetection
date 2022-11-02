import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

tipIds = [4, 8, 12, 16, 20]

# Define a function to 
def drawHandLanmarks(image, hand_landmarks):
    #print(hand_landmarks)
    # Draw connections between landmark points
    if hand_landmarks:

      for landmarks in hand_landmarks:
               
        mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)


def countFingers(image, hand_landmarks, handNo=0):
    
    if hand_landmarks:
        # Get all Landmarks of the FIRST Hand VISIBLE
        landmarks = hand_landmarks[handNo].landmark
        #print(landmarks)

        # Count Fingers        
        fingers = []

        for lm_index in tipIds:
                # Get Finger Tip and Bottom y Position Value
                finger_tip_y = landmarks[lm_index].y 
                finger_bottom_y = landmarks[lm_index - 2].y
                print("finger_tip_y",finger_tip_y)
                print("finger_bottom_y",finger_bottom_y)

while True:
    success, image = cap.read()
    #image = cv2.flip(image, 1)
    output=hands.process(image)
    landmarks=output.multi_hand_landmarks
    drawHandLanmarks(image,landmarks)

    # Get Hand Fingers Position        
    countFingers(image, landmarks)

    cv2.imshow("Media Controller", image)
    # Quit the window on pressing Sapcebar key
    key = cv2.waitKey(1)
    if key == 32:
        break
    