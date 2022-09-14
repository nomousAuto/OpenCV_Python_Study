
import numpy as np, cv2

# 함수를 첫번째로 작성
# 마우스 콜백 함수(argument 5개)
def onMouse(event, x, y, flags, param):
    global title
    # 우클릭 시 빨간 원 생성
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 20, (0, 0, 255), -1)
        cv2.imshow(title, img)
    # 좌클릭 시 파란 원 생성
    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (x,y), (x+30, y+30), (255, 0, 0), -1)
        cv2.imshow(title, img)

# 흰색 윈도우창 생성
img = np.full((500, 500, 3), (255, 255, 255), np.uint8)
title = 'Huh Ji-hoon'
cv2.namedWindow(title)
        
while True:
    cv2.imshow(title, img)
    # 함수 콜백
    cv2.setMouseCallback(title, onMouse)
    
    if cv2.waitKey() == 27:
        break
        
cv2.destroyAllWindows()
