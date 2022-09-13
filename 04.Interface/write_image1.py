
import cv2

image = cv2.imread("C:/Users/JihoonHuh/Images/Road.JPG", cv2.IMREAD_COLOR)
if image is None:
    # 예외처리
    raise Exception("영상파일 읽기 에러")
    
# JPEG 화질 설정
params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 10)
# PNG 압축 레벨 설정
params_png = (cv2.IMWRITE_PNG_COMPRESSION, 9)

## 행렬을 영상파일로 저장
# 디폴트는 95
cv2.imwrite("C:/Users/JihoonHuh/Images/Road_test1.JPG", image)
# 지정한 화질로 저장
cv2.imwrite("C:/Users/JihoonHuh/Images/Road_test2.JPG", image, params_jpg)
cv2.imwrite("C:/Users/JihoonHuh/Images/Road_test3.PNG", image, params_png)
# BMP 파일로 저장
cv2.imwrite("C:/Users/JihoonHuh/Images/Road_test4.BMP", image)
print("저장 완료")
