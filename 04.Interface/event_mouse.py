
import numpy as np
import cv2

# 콜백함수 - 이벤트 내용 출력
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("마우스 왼쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("마우스 오른쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONUP:
        print("마우스 오른쪽 버튼 떼기")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("마우스 왼쪽 버튼 더블클릭")

# 초기 영상 생성
image = np.full((200, 300), 255, np.uint8)

# 윈도우 이름
title1, title2 = "Mouse Event1", "Mouse Event2"

while True:
    # 영상 보기
    cv2.imshow(title1, image)
    cv2.imshow(title2, image)

    # 마우스 콜백함수
    cv2.setMouseCallback(title1, onMouse)

    if cv2.waitKey() == 27:
        print('ESC')
        break

# 열린 모든 윈도우 제거
cv2.destroyAllWindows()
