
import numpy as np
import cv2

## switch case문을 사전(dictionary)으로 구현
switch_case = {
    # ord() 함수 : 문자 -> 아스키코드 변환
    ord('a') : "a키 입력",
    ord('b') : "b키 입력",
    0x41 : "A키 입력",
    
    # 0x42(16진수) -> 10진수 변환
    int('0x42', 16) : "B키 입력",
    # 0x250000
    2424832 : "왼쪽 화살표키 입력",
    # 0x260000
    2490368 : "윗쪽 화살표키 입력",
    # 0x270000
    2555904 : "오른쪽 화살표키 입력",
    # 0x280000
    2621440 : "아래쪽 화살표키 입력"
}

# 원소값 1인 행렬 생성
image = np.ones((200, 300), np.float)
# 윈도우 이름
cv2.namedWindow('Keyboard Event')
cv2.imshow("Keyboard Evnet", image)

# 무한 반복
while True:
    # 100ms 동안 키 이벤트 대기
    key = cv2.waitKeyEx(100)
    
    # ESC 키 누르면 종료
    if key == 27:
        break
    
    try:
        result = switch_case[key]
        print(result)
        
    except KeyError:
        result = -1
        
# 열린 모든 윈도우 제거
cv2.destroyAllWindows()
