
import import_ipynb
import numpy as np, cv2
# 함수 재사용 위한 임포트
from utils import put_string

# 밝기 조절 콜백 함수
def bright_bar(value):
    global capture
    # 밝기 설정
    capture.set(cv2.CAP_PROP_BRIGHTNESS, value)

# 대비 조절 콜백 함수
def contrast_bar(value):
    global capture
    # 대비 설정
    capture.set(cv2.CAP_PROP_CONTRAST, value)
    
### Camera Default Setting ### 
# 0번 카메라 연결
capture = cv2.VideoCapture(0)
# 예외 처리
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")
    
# 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
# 카메라 프레임 높이
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
# 자동 초점 중지
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)
# 프레임 밝기 초기화
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)
    
title = "Huh Ji-hoon"
cv2.namedWindow(title)
cv2.createTrackbar('bright', title, 0, 100, bright_bar)
cv2.createTrackbar('contrast', title, 0, 100, contrast_bar)
###############################


while True:
    # 카메라 영상 받기
    ret, frame = capture.read()
    if not ret:
        break
    
    if cv2.waitKey(30) >= 0:
        break
    
    # 카메라 속성 가져오기
    bright = int(capture.get(cv2.CAP_PROP_BRIGHTNESS))
    contrast = int(capture.get(cv2.CAP_PROP_CONTRAST))
    # 밝기 값 표시
    put_string(frame, 'brightness : ', (10, 240), bright)
    # 대비 값 표시
    put_string(frame, 'contrast : ', (10, 270), contrast)
    cv2.imshow(title, frame)
    
# 비디오 캡쳐 메모리 해제
capture.release()
# 모든 창 닫기
cv2.destroyAllWindows()
