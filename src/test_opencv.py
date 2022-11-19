import cv2
import os
import numpy as np


img = cv2.imread("01 front.jpg")

h = img.shape[0]
w = img.shape[1]


blank_image = np.zeros((h, w, 3), np.uint8)
mask = cv2.circle(blank_image, [838, 290], 100, [255, 255, 255], -1)
mask01 = mask / 255
result = img * mask01
cv2.imwrite("resul01.png", result)

# делаем маску
# img[:] = (0, 0, 0)
# mask = cv2.circle(img, [838, 290], 100, [255, 255, 255], -1)

# cv2.imwrite("mask.png", mask)
# # читем маску в одном канале и применяем
# mask = cv2.imread("mask.png", 0)
# res = cv2.bitwise_and(cv2.imread("01 front.jpg"), cv2.imread("01 front.jpg"), mask=mask)
# cv2.imwrite("result.png", res)
# os.remove("mask.png")

# cv2.imwrite("result1.png", final)

# img[0, 0] = [0, 0, 255]
# cv2.imwrite("result.png", img)


# img[0:50, 0:200] = [0, 0, 255]
# cv2.imwrite("result.png", img)
# print(img.shape)
# print(img[0, 0])


# result = cv2.resize(img, (int(h / 2), int(w / 2)))
# result = cv2.flip(img, 0)

# img2 = img[0:200, 0:500]
# cv2.imwrite("result2.png", img2)

# for c in range(3):
#     x = img[:, :, c]
#     cv2.imwrite(f"result{c}.png", x)
