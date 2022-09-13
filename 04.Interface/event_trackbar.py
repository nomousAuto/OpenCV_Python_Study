
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

# 영상 생성
image = np.zeros((300, 500), np.uint8)

while True:
    title = 'Trackbar Event'
    cv2.imshow(title, image)

    # 트랙바 콜백 함수 등록
    cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)
    
    if cv2.waitKey() == 27:
        print('ESC')
        break
        
# 열린 모든 윈도우 제거
cv2.destroyAllWindows()
