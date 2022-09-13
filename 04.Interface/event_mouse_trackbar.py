
import numpy as np
import cv2

# 트랙바 콜백 함수
def onChange(value):
    # 전역 변수 참조
    global image, title
    
    # 트랙바 값과 영상 화소값 차분
    add_value = value - int(image[0][0])
    print("추가 화소값: ", add_value)
    # 행렬과 스칼라 덧셈 수행
    image = image + add_value
    cv2.imshow(title, image)
    
# 마우스 콜백 함수
def onMouse(event, x, y, flags, param):
    # 전역 변수 참조
    global image, bar_name
    
    # 마우스 우버튼
    if event == cv2.EVENT_RBUTTONDOWN:
        if (image[0][0] < 246):
            image = image + 10
        # 트랙바 위치 변경
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)
        
    elif event == cv2.EVENT_LBUTTONDOWN:
        if (image[0][0] >= 10):
            image = image - 10
        # 트랙바 위치 변경
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)
        
image = np.zeros((300, 500), np.uint8)
# 윈도우 이름
title = "Trackbar & Mouse Event"
# 트랙바 이름
bar_name = 'Brightness'

while True:
    cv2.imshow(title, image)

    # 트랙바 콜백 함수
    cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)
    # 마우스 콜백 함수 등록
    cv2.setMouseCallback(title, onMouse)
    
    if cv2.waitKey() == 27:
        print('ESC')
        break
        
# 모든 윈도우 닫기
cv2.destroyAllWindows()
