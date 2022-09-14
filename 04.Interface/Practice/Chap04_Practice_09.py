

import numpy as np, cv2

img = np.full((600, 400, 3), (255, 255, 255), np.uint8)

cv2.rectangle(img, (100, 100), (300, 400), (0, 0, 255), -1)

while True:
    cv2.imshow('Huh Ji-hoon', img)
    
    if cv2.waitKey() == 27:
        break
    
cv2.destroyAllWindows()
