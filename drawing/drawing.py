import cv2
import numpy as np

img = cv2.imread('color.jpg', cv2.IMREAD_COLOR)

#cv2.line(image, first point, second point, color, thickness)
cv2.line(img, (0,0), (150,150), (255, 0, 0), 5)

#cv2.rectangle(image, coordinate1, diagonal coordinate, color, thickness) ==> -1 stands for fill object
#rectangle will be drawn over line
cv2.rectangle(img, (45, 25), (450, 150), (155, 255, 200), -1)

#cv2.circle(image, centre, radius, color, thickness) ==> -1 stands for fill object
#circle will be drawn over line and rectangle
cv2.circle(img, (150,150), 50, (255,0 ,255), -1)

pts = np.array([[0, 10], [60, 80], [30, 40], [20, 60], [35, 45]], np.int32)
#cv2.polylines(image, [points], bool whether we want to connect the last point to the first, color, thickness)
cv2.polylines(img, [pts], True, (0, 255, 240), 1)

font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(image, text, start point, font, height, color, thickness, lineType)
#lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected.
#cv2.LINE_AA gives anti-aliased line which looks great for curves.
cv2.putText(img, 'Hi there!', (250,250), font, 1, (255, 0, 0), 2, cv2.LINE_AA)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
