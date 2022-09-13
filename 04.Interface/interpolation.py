
import matplotlib.pyplot as plt
import numpy as np

# 보간 방법
methods = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36']
# 0~1사이 임의 난수 생성
grid = np.random.rand(5, 5)

# 서브 플롯들 생성
fig, axs = plt.subplots(nrows = 2, ncols = 3, figsize = (8, 6))

# 서브 플롯 순회
for ax, method in zip(axs.flat, methods):
    # 명암도 영상 표시
    ax.imshow(grid, interpolation = method, cmap='gray')
    # 서브 플롯 제목
    ax.set_title(method)
# 여백 없음
plt.tight_layout()
# 윈도우 띄움
plt.show()
