#from RelevantAreas.Marking.MarkingRectangular import MarkingRectangular
from RelevantAreas.RelevantAreas import RelevantAreas
import cv2
import numpy as np

def nothing(x):
    pass

refPt = []
refMon = [(0,0),(0,0)]
cropping = False

def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, refMon, cropping
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        refMon[0] = (x, y)
        cropping = True
        
    elif event == cv2.EVENT_MOUSEMOVE:
        refMon[1] = (x, y)
        
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
        # draw a rectangle around the region of interest
        #cv2.rectangle(frame, refPt[0], refPt[1], (0, 255, 0), 2)


cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars", cv2.WINDOW_NORMAL)

cv2.createTrackbar("L - H", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - S", "Trackbars", 91, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 117, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 84, 255, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 229, 255, nothing)
cv2.createTrackbar("larger area", "Trackbars", 6000, 6000, nothing)
cv2.createTrackbar("smaller area", "Trackbars", 207, 6000, nothing)

#--------- MarkingRectangular--------
#MarkingRectangular01 = MarkingRectangular((255, 0, 0))
relevantAreas = RelevantAreas();

while True:
    #--------- Fonte de imagens ---------
    _, frame = cap.read()
    #frame = cv2.imread('img\IMG_7147.jpg',cv2.IMREAD_COLOR)
    #frame = cv2.imread('img\IMG_7134.jpg',cv2.IMREAD_COLOR)

  
    #--------- Area de analise ---------
    if len(refPt) == 2:
        cv2.rectangle(frame, refPt[0], refPt[1], (0, 255, 0), 2)

    if cropping == True:
        cv2.rectangle(frame, refMon[0], refMon[1], (0, 255, 255), 2)

    if len(refPt) == 2:
        frame = frame[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]       

    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")
    largerArea = cv2.getTrackbarPos("larger area", "Trackbars")
    smallerArea = cv2.getTrackbarPos("smaller area", "Trackbars")

    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #hsv =cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    #cropped = frame[100:1200,20:1500]


    maskYellow = cv2.inRange(hsv, lower_blue, upper_blue)
    maskYellow = cv2.erode(maskYellow, None, iterations=2)
    maskYellow = cv2.dilate(maskYellow, None, iterations=2)

    #dibujar(maskYellow, (255, 0, 0))
    #MarkingRectangular01.Marking(maskYellow, frame, largerArea, smallerArea)
    relevantAreas.Marking(maskYellow, frame, largerArea, smallerArea)

    #cntYellow = cv2.findContours(maskYellow.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    #centerYellow = None

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    cv2.setMouseCallback("frame", click_and_crop)

    key = cv2.waitKey(1)
    if key == 27:
        break

# cap.release()
cv2.destroyAllWindows()
