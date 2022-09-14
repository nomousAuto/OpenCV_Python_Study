
import numpy as np, cv2

# 300행, 400열의 행렬을 회색 바탕색(100)으로 생성
img = np.full((300, 400, 3), (100, 100, 100), np.uint8)


title = 'Hi'
cv2.namedWindow(title)
# 500행, 600열의 윈도우에 표시
cv2.moveWindow(title, 600, 500)

while True:
    cv2.imshow(title, img)
    
    if cv2.waitKey() == 27:
        break
        
cv2.destroyAllWindows()
