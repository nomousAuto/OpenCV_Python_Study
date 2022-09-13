
import import_ipynb
import cv2
# 함수 재사용 위한 임포트
from utils import put_string

# 줌 조절 콜백 함수
def zoom_bar(value):
    global capture
    # 줌 설정
    capture.set(cv2.CAP_PROP_ZOOM, value)
    
# 초점 조절 콜백 함수
def focus_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_FOCUS, value)

### Camera Default Setting ###
# 0번 카메라 연결
capture = cv2.VideoCapture(0)
if capture.isOpened == False:
    # 예외처리
    raise Exception("카메라 연결 안 됨")
    
# 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
# 카메라 프레임 높이
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
# 자동초점 중지
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)
# 프레임 밝기 초기화
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)
################################


# 윈도우 이름 지정
title = 'Change Camera Properties'
# 윈도우 생성
cv2.namedWindow(title)
# 줌 트랙바
cv2.createTrackbar('zoom', title, 0, 10, zoom_bar)
# 포커스 트랙바
cv2.createTrackbar('focus', title, 0, 40, focus_bar)

while True:
    # 카메라 영상 받기
    ret, frame = capture.read()
    if not ret:
        break
    
    if cv2.waitKey(30) >= 0:
        break
    
    # 카메라 속성 가져오기
    zoom = int(capture.get(cv2.CAP_PROP_ZOOM))
    focus = int(capture.get(cv2.CAP_PROP_FOCUS))
    # 줌 값 표시
    put_string(frame, 'zoom : ', (10, 240), zoom)
    # 초점 값 표시
    put_string(frame, 'focus : ', (10, 270), focus)
    cv2.imshow(title, frame)
    
# 비디오 캡처 메모리 해제
capture.release()
cv2.destroyAllWindows()
