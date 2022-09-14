
import numpy as np, cv2

# 문제점 : pt값 미설정
pt = (50, 50)
def onMouse(event, x, y, flags, param):
    global title, pt
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, pt, 50, 100, 1)
        # 문제점 : imshow 미사용
        cv2.imshow(title, image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        # 문제점 : right-bottom point 설정오류, RGB값 설정오류
        cv2.rectangle(image, pt, (130, 130), (100, 100, 100), 2)
        cv2.imshow(title, image)
    
image = np.ones((300, 300), np.uint8) * 255

title = "Draw Event"
cv2.namedWindow(title)

while True:
    cv2.imshow(title, image)
    cv2.setMouseCallback(title, onMouse)
    
    if cv2.waitKey() == 27:
        break
    
cv2.destroyAllWindows()
