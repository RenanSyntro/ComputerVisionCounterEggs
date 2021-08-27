import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

class element: 
    def __init__(self, box, x, y): 
        self.box = box 
        self.x = x
        self.y = y

class Contours:
    def __init__(self):
        self.box = 0
        self.x = 0
        self.y = 0
        self.contoursList = []

    def Marking(self, mask, largerArea, smallerArea):
        '''
        contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        '''
        contornos = cv2.findContours(
            mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        for c in contornos:
            area = cv2.contourArea(c)
            if len(c) > 0:
                if area > smallerArea and area < largerArea:
                    #cYellow = max(c, key=cv2.contourArea)
                    rectYellow = cv2.minAreaRect(c)  # cYellow
                    boxYellow = cv2.boxPoints(rectYellow)
                    boxYellow = np.int0(boxYellow)
                    self.box = boxYellow

                    MYellow = cv2.moments(c)  # cYellow
                    self.x = int(MYellow["m10"] / MYellow["m00"])
                    self.y = int(MYellow["m01"] / MYellow["m00"])

                    self.contoursList.append(element(self.box, self.x, self.y))
                #else:
                #    self.box = 0
                #    self.x = 0
                #    self.y = 0
                #    self.contoursList.clear()

                    #cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)
                    #cv2.drawContours(frame, [boxYellow], 0, (0, 255, 255), 2)
                    #cv2.putText(frame, '{},{}'.format(x, y), (x+10, y),
                    #            font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)


