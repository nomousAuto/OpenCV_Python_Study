
import cv2
# pyplot 모듈 임포트
import matplotlib.pyplot as plt

# 영상 읽기
image = cv2.imread("C:/Users/JihoonHuh/Images/Lee.PNG", cv2.IMREAD_COLOR)
# 예외 처리
if image is None:
    raise Exception("영상파일 읽기 에러")

# 영상 크기 정보
rows, cols = image.shape[:2]

# 컬러 공간 변환
rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# 명암도 영상 변환
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 그림 생성
fig = plt.figure(num = 1, figsize = (3, 4))
# 그림 표시 및 제목
plt.imshow(image)
plt.title('figure1- original(bgr)')
# 축 없음, 여백 없음
plt.axis('off')
plt.tight_layout()

# 그림 생성
fig = plt.figure(figsize = (6, 4))
# 전체 제목 지정
plt.suptitle('figure2- pyplot image display')
# 서브 플롯 그림
plt.subplot(1, 2, 1)
plt.imshow(rgb_img)
# 축 범위, 서브 플롯 제목
plt.axis([0, cols, rows, 0])
plt.title('rgb color')
# 서브 플롯 그림, 명암도로 표시
plt.subplot(1, 2, 2)
plt.imshow(gray_img, cmap='gray')
plt.title('gray_img2')
# 전체 그림 띄우기
plt.show()
