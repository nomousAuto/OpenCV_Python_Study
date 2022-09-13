
import numpy as np
import cv2

# 색상 지정
olive, violet, brown = (128, 128, 0), (221, 160, 221), (42, 42, 165)

# 문자열 위치 좌표
pt1, pt2 = (50, 230), (50, 310)

image = np.zeros((350, 500, 3), np.uint8)
image.fill(255)

cv2.putText(image, 'SIMPLEX', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, brown)
cv2.putText(image, 'DUPLEX', (50, 130), cv2.FONT_HERSHEY_DUPLEX, 3, olive)
cv2.putText(image, 'TRIPLEX', pt1, cv2.FONT_HERSHEY_DUPLEX, 3, violet)

# 글자체 상수
fontFace = cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC
cv2.putText(image, 'ITALIC', pt2, fontFace, 4, violet)


while True:
    # 윈도우 이름 지정 및 영상 표시
    cv2.imshow('Put Text', image)

    if cv2.waitKey() == 27:
        print('ESC')
        break

cv2.destroyAllWindows()
