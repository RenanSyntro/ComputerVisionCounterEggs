import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

class MarkingRectangular:
    def __init__(self, color):
        self.color = color

    def Marking(self, mask, frame, largerArea, smallerArea):
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
                    MYellow = cv2.moments(c)  # cYellow
                    x = int(MYellow["m10"] / MYellow["m00"])
                    y = int(MYellow["m01"] / MYellow["m00"])
                    cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)
                    cv2.drawContours(frame, [boxYellow], 0, (0, 255, 255), 2)
                    cv2.putText(frame, '{},{}'.format(x, y), (x+10, y),
                                font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)
                    # cv2.putText(frame,'X-M10 {:.1f}'.format(MYellow["m10"]),(x+10,y+20), font, 0.75,(0,0,255),1,cv2.LINE_AA) #str(MYellow["m10"])
                    #cv2.putText(frame,'X-M00 {:.1f}'.format(MYellow["m00"]),(x+10,y+40), font, 0.75,(0,0,255),1,cv2.LINE_AA)
                    #cv2.putText(frame,'Y-M01 {:.1f}'.format(MYellow["m01"]),(x+10,y+60), font, 0.75,(0,0,255),1,cv2.LINE_AA)
                    #cv2.putText(frame,'Y-M10 {:.1f}'.format(MYellow["m00"]),(x+10,y+80), font, 0.75,(0,0,255),1,cv2.LINE_AA)

            # projeto indeitifica por forma
            '''
            if area > 3000:
            M = cv2.moments(c)
            if (M["m00"]==0): M["m00"]=1
            x = int(M["m10"]/M["m00"])
            y = int(M['m01']/M['m00'])
            cv2.circle(frame,(x,y),7,(0,255,0),-1)
            cv2.putText(frame,'{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
            nuevoContorno = cv2.convexHull(c)
            cv2.drawContours(frame, [nuevoContorno], 0, color, 3)
        '''

        #desenha o círculo    
        preto = (0, 0, 0)
        cv2.circle(frame, (130, 230), 50, preto)
