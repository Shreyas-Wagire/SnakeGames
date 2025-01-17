import cvzone
import cv2
import numpy as np
import math
import random
from cvzone.HandTrackingModule import HandDetector

# Setup OpenCV capture and window size
capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

# Initialize hand detector
detect = HandDetector(detectionCon=0.8, maxHands=1)


class SnakeGame:
    def __init__(self, foodPath):
        self.points = []  # Points of the snake
        self.lengths = []  # Distance between points
        self.currentLength = 0  # Total snake length
        self.allowedLength = 150  # Maximum allowed length
        self.previousHead = (0, 0)  # Previous head point

        # Load food image
        self.foodImage = cv2.imread(foodPath, cv2.IMREAD_UNCHANGED)
        self.foodHeight, self.foodWidth, _ = self.foodImage.shape
        self.foodLocation = (0, 0)
        self.randomizeFoodLocation()
        self.score = 0
        self.gameOver = False

    def randomizeFoodLocation(self):
        self.foodLocation = random.randint(100, 1000), random.randint(100, 600)

    def update(self, imgMain, currentHead):
        if self.gameOver:
            cvzone.putTextRect(imgMain, "Game Over", [250, 350], scale=8, thickness=4,
                               colorT=(255, 255, 255), colorR=(0, 0, 255), offset=20)
            cvzone.putTextRect(imgMain, f'Your Score: {self.score}', [250, 500], scale=8, thickness=5,
                               colorT=(255, 255, 255), colorR=(0, 0, 255), offset=20)
        else:
            # Add new point and calculate distance
            px, py = self.previousHead
            cx, cy = currentHead
            self.points.append([cx, cy])
            distance = math.hypot(cx - px, cy - py)
            self.lengths.append(distance)
            self.currentLength += distance
            self.previousHead = cx, cy

            # Reduce length if exceeding allowed length
            while self.currentLength > self.allowedLength:
                self.currentLength -= self.lengths.pop(0)
                self.points.pop(0)

            # Check for food collision
            fx, fy = self.foodLocation
            if fx - self.foodWidth // 2 < cx < fx + self.foodWidth // 2 and fy - self.foodHeight // 2 < cy < fy + self.foodHeight // 2:
                self.randomizeFoodLocation()
                self.allowedLength += 50
                self.score += 1

            # Draw snake
            if self.points:
                for i in range(1, len(self.points)):
                    cv2.line(imgMain, tuple(self.points[i - 1]), tuple(self.points[i]), (0, 255, 0), 20)  # Green snake body
                cv2.circle(imgMain, self.points[-1], 20, (0, 128, 0), cv2.FILLED)  # Darker green snake head


            # Check for collision with itself
            pts = np.array(self.points[:-2], np.int32).reshape((-1, 1, 2))
            cv2.polylines(imgMain, [pts], False, (0, 200, 0), 3)
            minDist = cv2.pointPolygonTest(pts, (cx, cy), True)
            if minDist >= -1 and minDist <= 1:
                self.gameOver = True
                self.resetGame()

            # Draw food
            imgMain = cvzone.overlayPNG(imgMain, self.foodImage,
                                        (fx - self.foodWidth // 2, fy - self.foodHeight // 2))

            # Display score
            cvzone.putTextRect(imgMain, f'Score: {self.score}', [50, 80], scale=3, thickness=3, offset=10)

        return imgMain

    def resetGame(self):
        self.points = []
        self.lengths = []
        self.currentLength = 0
        self.allowedLength = 150
        self.previousHead = (0, 0)
        self.randomizeFoodLocation()
        self.score = 0
        self.gameOver = False


# Initialize game
game = SnakeGame("Donut.png")

# Main loop
while True:
    success, img = capture.read()
    img = cv2.flip(img, 1)  # Flip the camera horizontally
    hands, img = detect.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        pointIndex = lmList[8][0:2]  # Index finger tip location
        img = game.update(img, pointIndex)

    cv2.imshow("Snake Game", img)

    key = cv2.waitKey(1)
    if key == ord('r'):  # Restart game
        game.resetGame()
    if key == ord('q'):  # Quit game
        break

# Cleanup
capture.release()
cv2.destroyAllWindows()
