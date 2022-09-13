
# 넘파이 라이브러리 임포트
import numpy as np
# OpenCV 라이브러리 임포트
import cv2

# 행렬 생성
image = np.zeros((200, 400), np.uint8)
# 밝은 회색(200) 바탕 영상 생성
image[:] = 200

# 윈도우 이름
title1, title2 = 'Position1', 'Position2'
# 윈도우 생성 및 크기 조정 옵션
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2)

# 윈도우 이동 - 위치 지정
cv2.moveWindow(title1, 150, 150)
cv2.moveWindow(title2, 400, 50)

while True:
    # 행렬 원소를 영상으로 표시
    cv2.imshow(title1, image)
    cv2.imshow(title2, image)
    
    # 'ESC' 누르면 종료
    if cv2.waitKey() == 27:
        print('ESC')
        break

# 열린 모든 윈도우 파괴
cv2.destroyAllWindows()
