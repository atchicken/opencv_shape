import cv2
import numpy as np

import inspect

def main():
    """
    shape.py's main
    
    Note:
        * History
        2021/12/06: Create New
    """
    
    CreateRectangle()
    CreateLine()
    CreateArrowedLine()
    CreateCircle()
    CreateEllipse()
    CreateMarker()
    CreatePolygon()
    CreateText()
    
    return
    

def CreateRectangle():
    """
    Draw Rectangle
    
    Note:
        img = cv2.rectangle(img, coor1, coor2, color, thickness)
        coor1 (tuple): Upper Left Coordinates
        coor2 (tuple): Bottom Right Coordinates
    """
    
    img = np.full((128, 128, 3), 255, dtype=np.uint8)
    cv2.rectangle(img, (20, 10), (120, 40), (0, 255, 0))
    cv2.rectangle(img, (40, 55), (125, 80), (0, 255, 255), thickness=2)
    cv2.rectangle(img, (10, 95), (125, 110), (0, 0, 255), thickness=-1)
    cv2.imwrite("./rectangle.jpg", img)
    
    return


def CreateLine():
    """
    Draw Line
    
    Note:
        img = cv2.line(img, coor1, coor2, color, thickness)
        coor1 (tuple): Start Coordinates
        coor2 (tuple): End Coordinates
    """
    
    img = np.full((128, 128, 3), 255, dtype=np.uint8)
    cv2.line(img, (20, 10), (120, 40), (0, 255, 0))
    cv2.line(img, (40, 55), (125, 80), (0, 255, 255), thickness=2)
    cv2.line(img, (10, 95), (125, 110), (0, 0, 255), thickness=4)
    cv2.imwrite("./line.jpg", img)

    return


def CreateArrowedLine():
    """
    Draw ArrowedLine
    
    Note:
        img = cv2.arrowedLine(img, coor1, coor2, color, thickness)
        coor1 (tuple): Start Coordinates
        coor2 (tuple): End Coordinates
    """
    
    img = np.full((128, 128, 3), 255, dtype=np.uint8)
    cv2.arrowedLine(img, (20, 10), (120, 40), (0, 255, 0))
    cv2.arrowedLine(img, (40, 55), (125, 80), (0, 255, 255), thickness=2)
    cv2.arrowedLine(img, (10, 95), (125, 110), (0, 0, 255), thickness=4)
    cv2.imwrite("./arrowedLine.jpg", img)

    return
    

def CreateCircle():
    """
    Draw Circle
    
    Note:
        img = cv2.circle(img, coor, radius, color, thickness)
        coor (tuple): Center Coordinates
    """
    
    img = np.full((128, 128, 3), 255, dtype=np.uint8)
    cv2.circle(img, (20, 10), 2, (0, 255, 0))
    cv2.circle(img, (40, 55), 10, (0, 255, 255), thickness=2)
    cv2.circle(img, (10, 95), 20, (0, 0, 255), thickness=-1)
    cv2.imwrite("./circle.jpg", img)

    return


def CreateEllipse():
    """
    Draw Ellipse
    
    Note:
        img = cv2.ellipse(img, (coor, diameter, degree), color, thickness)
        coor     (tuple): Center Coordinates
        diameter (tuple): (X Length, Y Length)
    """
    
    img = np.full((128, 128, 3), 255, dtype=np.uint8)
    cv2.ellipse(img, ((20, 10), (5, 10), 0), (0, 255, 0))
    cv2.ellipse(img, ((40, 55), (25, 80), 20), (0, 255, 255), thickness=2)
    cv2.ellipse(img, ((10, 95), (25, 110), 90), (0, 0, 255), thickness=4)
    cv2.imwrite("./ellipse.jpg", img)

    return



def CreateMarker():
    """
    Draw Marker
    
    Note:
        img = cv2.drawMarker(img, coor, color, markerType, markerSize, thickness)
        coor (tuple): Center Coordinates
        markerType  : cv2.MARKER_CROSS(or None) -> +
                      cv2.MARKER_TILTED_CROSS   -> *
                      cv2.MARKER_STAR           -> ⭐︎
                      cv2.MARKER_DIAMOND        -> ♢
                      cv2.MARKER_SQUARE         -> □
                      cv2.MARKER_TRIANGLE_UP    -> △
                      cv2.MARKER_TRIANGLE_DOWN  -> ▽
    """
    
    img = np.full((128, 128, 3), 255, dtype=np.uint8)
    cv2.drawMarker(img, (20, 10), (0, 255, 0), markerType=cv2.MARKER_TILTED_CROSS)
    cv2.drawMarker(img, (40, 55), (0, 255, 255), markerType=cv2.MARKER_DIAMOND, markerSize=20)
    cv2.drawMarker(img, (10, 95), (0, 0, 255), thickness=4)
    cv2.drawMarker(img, (40, 100), (255, 255, 0),
                   markerType=cv2.MARKER_STAR)
    cv2.drawMarker(img, (30, 30), (255, 0, 0),
                   markerType=cv2.MARKER_DIAMOND)
    cv2.drawMarker(img, (70, 50), (0, 255, 128),
                   markerType=cv2.MARKER_SQUARE)
    cv2.drawMarker(img, (100, 80), (128, 255, 0),
                   markerType=cv2.MARKER_TRIANGLE_UP)
    cv2.drawMarker(img, (120, 110), (0, 128, 128),
                   markerType=cv2.MARKER_TRIANGLE_DOWN)

    cv2.imwrite("./marker.jpg", img)

    return




def CreatePolygon():
    """
    Draw Polygon
    
    Note:
        img = cv2.polylines(img, (coor, diameter, degree), color, thickness)
        coor     (tuple): Center Coordinates
        diameter (tuple): (X Length, Y Length)
    
        img = cv2.fillPoly(img, [pts], color)
        pts (list): List of numpy.ndarray(2D Array)
        * "thickness" can not use
         
        img = cv2.fillConvexPoly(img, pts, color)
        pts (numpy.ndarray): 2D Array
    """
    
    img = np.full((128, 128, 3), 255, dtype=np.uint8)
    pts = np.array(((20, 10), (25, 50), (40, 100)))
    cv2.polylines(img, [np.array(((20, 10), (25, 50), (60, 40)))],
                  True, (0, 255, 0))
    cv2.polylines(img, [np.array(((70, 10), (75, 50), (110, 40)))],
                  False, (0, 255, 255), thickness=4)
    cv2.fillPoly(img, [np.array(((20, 50), (25, 80), (60, 110), (50, 120),
                                 (10, 100)))], (0, 0, 255))
    cv2.fillConvexPoly(img, np.array(((70, 50), (75, 80), (110, 110),
                                      (100, 120), (60, 100))), (255, 255, 0))
    cv2.imwrite("./polygon.jpg", img)

    return




def CreateText():
    """
    Draw Text

    Note:
       img = cv2.putText(img, text, coor, fontType, size, color, thickness)
       text   (str): Draw Text(Can't Use Japanese)
       coor (tuple): Bottom Left Coordinates
       fontType    : cv2.FONT_HERSHEY_SIMPLEX
                     cv2.FONT_HERSHEY_PLAIN
                     cv2.FONT_HERSHEY_DUPLEX
                     cv2.FONT_HERSHEY_COMPLEX
                     cv2.FONT_HERSHEY_TRIPLEX
                     cv2.FONT_HERSHEY_COMPLEX_SMALL
                     cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
                     cv2.FONT_HERSHEY_SCRIPT_COMPLEX
                     cv2.FONT_ITALIC
    """

    img = np.full((128, 128, 3), 255, dtype=np.uint8)
    cv2.putText(img, "test", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 0, 0), thickness=2)
    cv2.putText(img, "test", (10, 45), cv2.FONT_HERSHEY_PLAIN, 0.7,
                (255, 0, 0), thickness=2)
    cv2.putText(img, "test", (10, 70), cv2.FONT_HERSHEY_DUPLEX, 0.7,
                (255, 0, 0), thickness=2)
    cv2.putText(img, "test", (10, 95), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                (255, 0, 0), thickness=2)
    cv2.putText(img, "test", (10, 120), cv2.FONT_HERSHEY_TRIPLEX, 0.7,
                (255, 0, 0), thickness=2)
    cv2.putText(img, "test", (65, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7,
                (255, 0, 0), thickness=2)
    cv2.putText(img, "test", (65, 45), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.7,
                (255, 0, 0), thickness=2)
    cv2.putText(img, "test", (65, 70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.7,
                (255, 0, 0), thickness=2)
    cv2.putText(img, "test", (65, 95), cv2.FONT_ITALIC, 0.7,
                (255, 0, 0), thickness=2)
    cv2.imwrite("./text.jpg", img)
    


if __name__ == "__main__":
    main()
