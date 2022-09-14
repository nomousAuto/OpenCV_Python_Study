
import numpy as np, cv2

img = cv2.imread("C:/Users/JihoonHuh/Images/Lee.PNG", cv2.IMREAD_GRAYSCALE)
# 예외처리
if img is None:
    raise Exception("영상파일 읽기 에러")

# JPEG 화질 설정
params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 100)
# PNG 압축 설정
params_png = (cv2.IMWRITE_PNG_COMPRESSION, 9)


cv2.imwrite("C:/Users/JihoonHuh/Images/test.JPG", img, params_jpg)
cv2.imwrite("C:/Users/JihoonHuh/Images/test.PNG", img, params_png)
