
import cv2

# 문자열 출력 함수
def put_string(frame, text, pt, value, color = (120, 200, 90)):
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # 그림자 효과
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)
    # 글자 적기
    cv2.putText(frame, text, pt, font, 0.7, color, 2)
    
# 0번 카메라 연결
capture = cv2.VideoCapture(0)
# 카메라 연결 예외처리
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")
    

## 카메라 속성 획득 및 출력
print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))

# 무한 반복
while True:
    # 카메라 영상 밝기
    ret, frame = capture.read()
    if not ret:
        break
    # 종료 조건 - 스페이스바 키
    if cv2.waitKey(30) >= 0:
        break
    
    # 노출 속성 획득
    exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
    put_string(frame, 'EXPOS: ', (10, 40), exposure)
    title = "View Frame from Camera"
    # 윈도우에 영상 띄우기
    cv2.imshow(title, frame)

capture.release()
cv2.destroyAllWindows()
