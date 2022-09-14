
import numpy as np, cv2

img1 = np.full((200, 300, 3), (0, 0, 0), np.uint8)
img2 = np.full((200, 300, 3), (0, 0, 0), np.uint8)

title1 = "win mode1"
title2 = "win mode2"
cv2.namedWindow(title1)
cv2.namedWindow(title2)

cv2.moveWindow(title1, -17, 0)
cv2.moveWindow(title2, 280, 200)

while True:
    cv2.imshow(title1, img1)
    cv2.imshow(title2, img2)
    
    if cv2.waitKey() == 27:
        break
    
cv2.destroyAllWindows()
