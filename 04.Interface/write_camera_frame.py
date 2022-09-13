
import cv2


### Camera Default Setting ###
# 0번 카메라 연결
capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")
    
# 초당 프레임 수
fps = 29.97
# 프레임 간 지연 시간
delay = round(1000/fps)
# 동영상파일 해상도
size = (640, 360)
# 압축 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'DX50')
###############################


## 카메라 속성 실행창에 출력
print("width x height: ", size)
print("VideoWriterfourcc: %s" % fourcc)
print("delay: %2d ms" % delay)
print("fps: %.2f" % fps)

# 카메라 속성 지정
capture.set(cv2.CAP_PROP_ZOOM, 1)
capture.set(cv2.CAP_PROP_FOCUS, 0)
# 해상도 설정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])

## 동영상파일 개방 및 코덱, 해상도 설정
writer = cv2.VideoWriter("C:/Users/JihoonHuh/Images/video_test.avi", fourcc, fps, size)
if writer.isOpened() == False:
    raise Exception("동영상 파일 개방 안됨")
    
while True:
    # 카메라 영상 받기
    ret, frame = capture.read()
    if not ret:
        break
    if cv2.waitKey(delay) >= 0:
        break
    
    # 프레임을 동영상으로 저장
    writer.write(frame)
    cv2.imshow("View Frame from Camera", frame)
    
writer.release()
capture.release()
