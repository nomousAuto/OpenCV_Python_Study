
import numpy as np, cv2

img = np.full((400, 600, 3), (255, 255, 255), np.uint8)

title = 'image'
cv2.namedWindow(title)

# 빨간색 큰 반원 그리기
cv2.ellipse(img, (300, 200), (100, 100), 0, 0, -180, (0, 0, 255), -1)
# 파란색 큰 반원 그리기
cv2.ellipse(img, (300, 200), (100, 100), 0, 0, 180, (255, 0, 0), -1)
# 빨간색 작은 반원 그리기
cv2.ellipse(img, (250, 200), (50, 50), 0, 0, 180, (0, 0, 255), -1)
# 파란색 작은 반원 그리기
cv2.ellipse(img, (350, 200), (50, 50), 0, 0, -180, (255, 0, 0), -1)


while True:
    cv2.imshow(title, img)
    
    if cv2.waitKey() == 27:
        break
        
cv2.destroyAllWindows()
