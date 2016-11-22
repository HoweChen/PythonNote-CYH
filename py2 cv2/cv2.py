import cv2
import numpy as np

img = cv2.imread('/Users/howechen/GitHub/PythonNote-CYH/pyTest/Lenna.png')
cv2.imshow('image', img)
print cv2.__version__
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('/Users/howechen/GitHub/PythonNote-CYH/pyTest/LennaV2.png', img)
    cv2.destroyAllWindows()
