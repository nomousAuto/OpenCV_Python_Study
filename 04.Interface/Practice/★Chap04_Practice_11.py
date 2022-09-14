
import numpy as np, cv2

    
# 마우스 콜백 함수(argument 5개)
def onMouse(event, x, y, flags, param):
    global title, line, radius
    # 우클릭 시 빨간 원 생성
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), radius, (0, 0, 255), line)
        cv2.imshow(title, img)
    # 좌클릭 시 파란 원 생성
    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (x,y), (x+30, y+30), (255, 0, 0), line)
        cv2.imshow(title, img)

# 굵기 조절 콜백 함수
def line_bar(value):
    global line
    print(value)
    line = value
    
# 원 반지름 조절 콜백 함수
def radius_bar(value):
    global radius
    print(value)
    radius = value


# 흰색 윈도우창 생성
img = np.full((500, 500, 3), (255, 255, 255), np.uint8)
title = 'Huh Ji-hoon'
cv2.namedWindow(title)

# 굵기와 원 반지름 초기값
line = 2
radius = 20

while True:
    cv2.imshow(title, img)
    
    ### trackbar setting ###
    cv2.createTrackbar('Line', title, 2, 10, line_bar)
    cv2.setTrackbarMin('Line', title, 1)

    cv2.createTrackbar('Radius', title, 20, 50, radius_bar)
    cv2.setTrackbarMin('Radius', title, 1)
    ########################
    
    # 함수 콜백
    cv2.setMouseCallback(title, onMouse)
    
    if cv2.waitKey() == 27:
        break
        
cv2.destroyAllWindows()

# Source : https://min-wachya.tistory.com/100?category=830312
