
import numpy as np
import cv2

# 마우스 콜백 함수
def onMouse(event, x, y, flags, param):
    global title
    # 휠 버튼을 누르면 타원 생성
    if event == cv2.EVENT_MBUTTONDOWN:
        cv2.ellipse(img, (x,y), (120, 60), 0, 0, 360, (0, 0, 255), -1)
        cv2.imshow(title, img)
        
img = np.full((500, 500, 3), (255, 255, 255), np.uint8)
title = 'Huh Ji-hoon'
cv2.namedWindow(title)

while True:
    cv2.imshow(title, img)
    cv2.setMouseCallback(title, onMouse)
    
    if cv2.waitKey() == 27:
        break
    
cv2.destroyAllWindows()
