
import matplotlib.pyplot as plt
import numpy as np

# x축 데이터
x = np.arange(10)
# y축 데이터
y1 = np.arange(10)
y2 = np.arange(10)**2
y3 = np.random.choice(50, size = 10)

# 그림 객체 생성 - 그래프 크기(단위 inch)
plt.figure(figsize = (5, 3))
# 선 스타일 지정 - 파란색, 파선
plt.plot(x, y1, 'b--', linewidth=2)
# 선 스타일 지정 - 녹색, 원마크, 실선
plt.plot(x, y2, 'go-', linewidth=3)
# 선 스타일 지정 - 청록색, +마크, 점선
plt.plot(x, y3, 'c+:', linewidth=5)

# 그래프 제목
plt.title('Line examples')
# 축 범위
plt.axis([0, 10, 0, 80])
plt.tight_layout()
# 그림 저장
plt.savefig(fname='sample.png', dpi=300)
# 윈도우 표시
plt.show()
