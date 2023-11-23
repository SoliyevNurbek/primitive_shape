from polygon import Polygon
from math import sqrt
class Triangle(Polygon):
    def __init__(self, height, width, c) -> None:
        super().__init__(height,width)
        self.c=c
    def getArea(self):
        p=(self.height+self.width+self.c)/2
        return sqrt(p*(p-self.height)*(p-self.width)*(p-self.c)) if self.height>0 and self.width>0 and self.c>0 and (self.height+self.width)>self.c and (self.height+self.c)>self.width and (self.width+self.c)>self.height else "Error"
    def getPerimeter(self):
        return (self.height+self.width+self.c) if self.height>0 and self.width>0 and self.c>0 and (self.height+self.width)>self.c and (self.height+self.c)>self.width and (self.width+self.c)>self.height else "Error"