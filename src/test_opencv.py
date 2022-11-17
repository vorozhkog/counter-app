import cv2

img = cv2.imread("01 front.jpg")
print(img.shape)
print(img[0, 0])

h = img.shape[0]
w = img.shape[1]
# result = cv2.resize(img, (int(h / 2), int(w / 2)))
# result = cv2.flip(img, 0)
result = cv2.circle(img, [850, 290], 100, [0, 0, 255], -1)
cv2.imwrite("result.png", result)
# img[0, 0] = [0, 0, 255]
# cv2.imwrite("result.png", img)


# img[0:50, 0:200] = [0, 0, 255]
# cv2.imwrite("result.png", img)

# img2 = img[0:200, 0:500]
# cv2.imwrite("result2.png", img2)

# for c in range(3):
#     x = img[:, :, c]
#     cv2.imwrite(f"result{c}.png", x)
