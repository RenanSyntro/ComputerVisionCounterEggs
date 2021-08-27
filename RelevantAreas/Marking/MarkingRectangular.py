from RelevantAreas.Contours import Contours
import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

class MarkingRectangular:
    def __init__(self, color):
        self.color = color

    def Marking(self, frame, elementsContors):
        '''
        contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        '''
        for c in elementsContors:
            if (np.any(c.box)):
                cv2.circle(frame, (c.x, c.y), 7, (0, 255, 0), -1)
                cv2.drawContours(frame, [c.box], 0, (0, 255, 255), 2)
                cv2.putText(frame, '{},{}'.format(c.x, c.y), (c.x+10, c.y),
                    font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)

                #desenha o círculo    
                preto = (0, 0, 0)
                cv2.circle(frame, (130, 230), 50, preto)

        elementsContors.clear()
