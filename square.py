from polygon import Polygon
class Square(Polygon):
    def __init__(self,a) -> None:
        super().__init__(a, a)
    def getArea(self):
        return super().getArea()
    def getPerimeter(self):
        return super().getPerimeter()