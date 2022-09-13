
import numpy as np
import cv2

# ndarray 행렬 생성
image = np.zeros((200, 300), np.uint8)
# 모든 원소에 255(흰색) 지정
image.fill(255)

# 윈도우 이름 변수
title1, title2 = 'AUTOSIZE', 'NORMAL'

# 윈도우 생성 - 크기변경 불가
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
# 크기 변경 가능
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)


while True:
    
    # 행렬 원소를 영상으로 표시
    cv2.imshow(title1, image)
    cv2.imshow(title2, image)

    # 윈도우 크기 변경
    cv2.resizeWindow(title1, 400, 300)
    cv2.resizeWindow(title2, 400, 300)
    
    # 'ESC' 버튼 누르면 종료
    if cv2.waitKey() == 27:
        print('ESC')
        break
    
# 열린 모든 윈도우 제거
cv2.destroyAllWindows()
