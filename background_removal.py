import numpy as np
import cv2

camera = cv2.VideoCapture(0)

camera.set(3 , 640)
camera.set(4 , 480)

mountain = cv2.imread('mountain.jpg')
mountain = cv2.resize(mountain , (640 , 480))

while True:
    status , frame = camera.read()

    if status:

        frame = cv2.flip(frame , 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # creating thresholds
        lower_bound = np.array([100,100,100])
        upper_bound = np.array([255,255,255])

        # thresholding image
        back = cv2.inRange(frame_rgb, lower_bound, upper_bound)

        # inverting the mask
        back = cv2.bitwise_not(back)

        # bitwise and operation to extract foreground / person
        person = cv2.bitwise_and(frame, frame , mask = back)

        # final image
        output = np.where(person  ==  0 , mountain , person)

        # show it
        cv2.imshow('Output' , output)

        # wait of 1ms before displaying another frame
        code = cv2.waitKey(1)
        if code  ==  32:
            break

camera.release()
cv2.destroyAllWindows()