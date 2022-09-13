
import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    # 전역 변수 참조
    global title, pt
    
    if event == cv2.EVENT_LBUTTONDOWN:
        # 시작 좌표 지정
        if pt[0] < 0:
            pt = (x, y)
        else:
            # 파란색 사각형
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
            cv2.imshow(title, image)
            pt = (-1, -1)
            
    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            # 두 좌표 간 간격
            dx, dy = pt[0] - x, pt[1] - y
            radius = int(np.sqrt(dx*dx + dy*dy))
            # 빨간색 원
            cv2.circle(image, pt, radius, (0, 0, 255), 2)
            cv2.imshow(title, image)
            # 시작 좌표 초기화
            pt = (-1, -1)
            
# 흰색 배경 영상
image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

# 시작 좌표 초기화
pt = (-1, -1)
title = "Draw Event"

while True:
    cv2.imshow(title, image)
    
    cv2.setMouseCallback(title, onMouse)
    if cv2.waitKey() == 27:
        print('ESC')
        break

cv2.destroyAllWindows()
