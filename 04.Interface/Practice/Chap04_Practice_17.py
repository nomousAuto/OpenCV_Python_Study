
import numpy as np, cv2

capture = cv2.VideoCapture(0)
if capture.isOpened is None:
    raise Exception("카메라 연결 안 됨")

# 초당 프레임 수
fps = 15
# 프레임 간 지연 시간
delay = round(1000/fps)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    
# 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# 카메라 프레임 높이
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

## 동영상 파일 개방 및 코덱 설정
writer = cv2.VideoWriter("C:/Users/JihoonHuh/Images/flip_test2.avi", fourcc, fps, (640, 480))
if writer.isOpened() == False:
    raise Exception("동영상 파일 개방 안 됨")
    
while True:
    # 카메라 영상 받기
    ret, frame = capture.read()
    if not ret:
        break
    if cv2.waitKey(delay) >= 0:
        break
    
    # 좌우 반전
    frame = cv2.flip(frame, 1)
    
    # 프레임을 동영상으로 저장
    writer.write(frame)
    cv2.imshow("View Frame from Camera", frame)
    
writer.release()
capture.release()
cv2.destroyAllWindows()
