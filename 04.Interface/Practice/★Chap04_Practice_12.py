
import numpy as np
import cv2

# 트랙바 콜백 함수
def onChange(value):
    # 전역 변수 참조
    global image, title
    
    # 트랙바의 현재 값을 리턴
    image[:] = cv2.getTrackbarPos('Brightness', title)
    cv2.imshow(title, image)
    
# 영상 생성
image = np.zeros((300, 500), np.uint8)

title = 'Trackbar Event'
cv2.imshow(title, image)

# 트랙바 콜백 함수 등록
cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)

while True:
    
    # cv2.waitKeyEx : 방향키같은 특수 키 처리 가능
    k = cv2.waitKeyEx(100)
    if k == 27:
        break

    # 왼쪽 화살표 키 입력
    if k == 2424832:
        # 트랙바의 현재 값을 리턴
        value = cv2.getTrackbarPos('Brightness', title)
        # 트랙바의 값을 설정
        cv2.setTrackbarPos('Brightness', title, value - 1)
        
    # 오른쪽 화살표 키 입력
    elif k == 2555904:
        # 트랙바의 현재 값을 리턴
        value = cv2.getTrackbarPos('Brightness', title)
        # 트랙바의 값을 설정
        cv2.setTrackbarPos('Brightness', title, value + 1)
        
    
cv2.destroyAllWindows()

# Source : https://min-wachya.tistory.com/100?category=830312
# Source : https://m.blog.naver.com/samsjang/220502125621
# Source : https://076923.github.io/posts/Python-opencv-35/
