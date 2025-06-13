import cv2
import mediapipe as mp
import numpy as np

class BlinkDetector:
    def __init__(self):
        self.faceMesh = mp.solutions.face_mesh.FaceMesh()
        self.LEFT_EYE = [33, 160, 158, 133, 153, 144]

    def euclidean(self, p1, p2):
        return np.linalg.norm(np.array(p1) - np.array(p2))

    def blink_ratio(self, landmarks):
        left = [landmarks[i] for i in self.LEFT_EYE]
        top = (left[1][1] + left[2][1]) / 2
        bottom = (left[4][1] + left[5][1]) / 2
        vertical = abs(top - bottom)
        horizontal = self.euclidean(left[0], left[3])
        return horizontal / vertical if vertical != 0 else 100

    def detect_blink(self, frame):
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(rgb)
        if results.multi_face_landmarks:
            landmarks = []
            for lm in results.multi_face_landmarks[0].landmark:
                landmarks.append((int(lm.x * w), int(lm.y * h)))
            return self.blink_ratio(landmarks)
        return 100
