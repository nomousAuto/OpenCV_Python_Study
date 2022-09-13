
import import_ipynb
import numpy as np
import cv2
# 행렬 정보 출력 함수 임포트
from utils import print_matInfo

title1, title2 = 'color2gray', 'color2color'
color2gray = cv2.imread("C:/Users/JihoonHuh/Images/Road.JPG", cv2.IMREAD_GRAYSCALE)
color2color = cv2.imread("C:/Users/JihoonHuh/Images/Road.JPG", cv2.IMREAD_COLOR)

# 예외처리
if color2gray is None or color2color is None:
    raise Exception("영상파일 읽기 에러")
    

print("행렬 좌표(100, 100) 화소값")
# 한 화소값 표시
print("%s %s" % (title1, color2gray[100, 100]))
print("%s %s\n" % (title2, color2color[100, 100]))

# 행렬 정보 출력
print_matInfo(title1, color2gray)
print_matInfo(title2, color2color)
# 행렬 정보 출력
cv2.imshow(title1, color2gray)
cv2.imshow(title2, color2color)

while True:    
    if cv2.waitKey() == 27:
        print('ESC')
        break
    
cv2.destroyAllWindows()
