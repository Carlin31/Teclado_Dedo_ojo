import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, maxHands=1):
        self.hands = mp.solutions.hands.Hands(max_num_hands=maxHands)
        self.mpDraw = mp.solutions.drawing_utils

    def find_index_finger(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                lm = hand.landmark[8]  # Índice
                h, w, _ = frame.shape
                return int(lm.x * w), int(lm.y * h)
        return None
