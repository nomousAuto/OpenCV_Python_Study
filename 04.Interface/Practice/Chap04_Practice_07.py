
import numpy as np, cv2

image = np.zeros((300, 400, 3), np.uint8)
image[:] = (255, 255, 255)

# 문제점 : line의 parameter 중 점과 RGB값이 생략됨
pt1, pt2 = (50, 130), (200, 200)
cv2.line(image, pt1, (100, 100), (100, 100, 100))
cv2.line(image, pt1, pt2, (100, 100, 100))
cv2.rectangle(image, pt1, pt2, (255, 0, 255))
cv2.rectangle(image, pt1, pt2, (0, 0, 255))

title = "Line & Rectangle"
cv2.namedWindow(title)

while True:
    cv2.imshow(title, image)
    
    if cv2.waitKey() == 27:
        break
    
cv2.destroyAllWindows()
