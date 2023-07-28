import cv2

img = cv2.imread("solar-system.jpg")
cv2.imshow("output", img)

cv2.putText(img, "Sun", (2, 300), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255))
cv2.putText(img, "Mercury", (120, 240), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))
cv2.putText(img, "Venus", (195, 175), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))
cv2.putText(img, "Earth", (290, 260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Mars", (385, 180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Jupiter", (525, 375), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
cv2.putText(img, "Saturn", (770, 130), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255))
cv2.putText(img, "Uranus", (963, 285), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255))
cv2.putText(img, "Neptune", (1095, 150), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255))

cv2.imwrite("Solar_systemwithname.jpg", img)

cv2.waitKey(0)
