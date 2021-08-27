from RelevantAreas.Contours.Contours import Contours
from RelevantAreas.Marking.MarkingRectangular import MarkingRectangular

contours = Contours()
markingRectangular = MarkingRectangular((0,0,255))

class RelevantAreas:
    def __init__(self):
        pass

    def Marking(self, maskYellow, frame, largerArea, smallerArea):
        contours.Marking(maskYellow, frame, largerArea, smallerArea)
        markingRectangular.Marking(frame, contours.box, contours.x, contours.y, contours.contoursList)

