
import numpy as np, cv2

# 0번 카메라 연결
capture = cv2.VideoCapture(0)
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

while True:
    ret, frame = capture.read()
    if not ret:
        break
    
    if cv2.waitKey(30) >= 0:
        break
    

    
    # 1), 3) (200, 100) 좌표에서 100 x 200 크기의 관심 영역 지정
    cv2.rectangle(frame, (200, 100), (300, 300), (0, 0, 255), 2)
    # 2) 관심 영역에서 녹색 성분을 50만큼 증가
    ######################################
    # 2-1) bgr을 분리한다
    blue, green, red = cv2.split(frame)
    # 2-2) cv2.add를 사용하여 green 채널의 일부 영역에 50을 더한다
    cv2.add(green[100:300, 200:300], 50, green[100:300, 200:300])
    # 2-3) channel들을 합친다
    frame = cv2.merge([blue, green, red])
    ######################################
    
    cv2.imshow(title, frame)
    
capture.release()
cv2.destroyAllWindows()


# SOURCE : https://min-wachya.tistory.com/100?category=830312#fourteen
