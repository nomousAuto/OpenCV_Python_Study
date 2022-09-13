
import import_ipynb
import cv2
# 글쓰기 함수 임포트
from utils import put_string

### Camera Default Setting ###
# 동영상 파일 개방
capture = cv2.VideoCapture("C:/Users/JihoonHuh/Images/video_test.avi")
# 예외 처리
if not capture.isOpened():
    raise Exception("동영상파일 개방 안됨")

# 초당 프레임 수
frame_rate = capture.get(cv2.CAP_PROP_FPS)
# 지연 시간
delay = int(1000/frame_rate)
# 현재 프레임 번호
frame_cnt = 0
###############################


while True:
    ret, frame = capture.read()
    # 프레임 간 지연 시간 지정
    if not ret or cv2.waitKey(delay) >= 0:
        break
    # 컬러 영상 채널 분리
    blue, green, red = cv2.split(frame)
    frame_cnt += 1
    
    # blue 채널 밝기 증가
    if 100 <= frame_cnt < 200:
        cv2.add(blue, 100, blue)
    # green 채널 밝기 증가
    elif 200 <= frame_cnt < 300:
        cv2.add(green, 100, green)
    # red 채널 밝기 증가
    elif 300 <= frame_cnt < 400:
        cv2.add(red, 100, red)
    
    # 단일채널 영상 합성
    frame = cv2.merge([blue, green, red])
    put_string(frame, 'frame_cnt: ', (20, 30), frame_cnt)
    cv2.imshow("Read Video File", frame)
    
capture.release()
