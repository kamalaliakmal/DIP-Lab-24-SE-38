"""Helper script: generates input_image.png (640x480), the test image used by the notebook.
It contains hard edges (checkerboard), curves, an asymmetric letter and an arrow so that
flips, rotations, shifts and interpolation differences are easy to see.
You may replace input_image.png with your own photo; the notebook works with any image."""
import numpy as np
import cv2

H, W = 480, 640
img = np.zeros((H, W, 3), np.uint8)                    # OpenCV drawing uses BGR order
top, bottom = np.array([250, 225, 200]), np.array([210, 190, 150])   # BGR
for y in range(H):
    t = y / (H - 1)
    img[y, :] = (top * (1 - t) + bottom * t).astype(np.uint8)

# checkerboard (mid-tone greys so interpolation overshoot is visible)
x0, y0, sq = 20, 20, 8
for r in range(15):
    for c in range(20):
        v = 60 if (r + c) % 2 == 0 else 200
        cv2.rectangle(img, (x0 + c * sq, y0 + r * sq), (x0 + (c + 1) * sq - 1, y0 + (r + 1) * sq - 1), (v, v, v), -1)

cv2.circle(img, (500, 130), 70, (60, 60, 220), -1, cv2.LINE_AA)                       # red circle
cv2.circle(img, (500, 130), 70, (255, 255, 255), 3, cv2.LINE_AA)
cv2.rectangle(img, (230, 40), (370, 140), (60, 170, 240), -1)                          # orange rectangle
cv2.fillPoly(img, [np.array([[230, 210], [300, 150], [370, 210]])], (70, 160, 60), cv2.LINE_AA)  # green triangle
cv2.putText(img, "DIP LAB 4", (170, 270), cv2.FONT_HERSHEY_DUPLEX, 1.8, (110, 40, 20), 3, cv2.LINE_AA)
cv2.putText(img, "F", (40, 440), cv2.FONT_HERSHEY_TRIPLEX, 5, (30, 30, 30), 8, cv2.LINE_AA)  # asymmetric letter
cv2.arrowedLine(img, (200, 440), (420, 340), (140, 40, 120), 8, cv2.LINE_AA, tipLength=0.25)
cv2.line(img, (450, 300), (620, 460), (40, 40, 40), 2, cv2.LINE_AA)                  # thin diagonal
cv2.rectangle(img, (0, 0), (W - 1, H - 1), (40, 40, 40), 2)                            # border
cv2.imwrite("input_image.png", img)
print("saved input_image.png", img.shape)
