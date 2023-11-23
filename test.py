from circle import Circle
from line import Line
from point import Point
from polygon import Polygon
from rectangle import Rectangle
from square import Square
from triangle import Triangle

circ=Circle(5)
circ_getarea=circ.getArea()
circ_getperim=circ.getLength()
# print(circ_getarea)
# print(circ_getperim)

lin=Line(1,2,4,6)
lin_getleng=lin.get_length()
# print(lin_getleng)

poin=Point(0,7)
poin_distansex=poin.distance_from_Xcoordinate()
poin_distansey=poin.distance_from_Ycoordinate()
poin_quadrat=poin.getQuadrant()
poin_onx=poin.on_Xcoordinate()
poin_ony=poin.on_Ycoordinate()
# print(poin_distansex)
# print(poin_distansey)
# print(poin_quadrat)
# print(poin_onx)
# print(poin_ony)

poly=Polygon(5,6)
poly_getarea=poly.getArea()
poly_getperim=poly.getPerimeter()
# print(poly_getarea)
# print(poly_getperim)

rect=Rectangle(7,8)
rect_getarea=rect.getArea()
rect_getperim=rect.getPerimeter()
# print(rect_getarea)
# print(rect_getperim)

squar=Square(9)
squar_getarea=squar.getArea()
squar_getperim=squar.getPerimeter()
# print(squar_getarea)
# print(squar_getperim)


trian=Triangle(6,8,10)
trian_getarea=trian.getArea()
trian_getperim=trian.getPerimeter()
# print(trian_getarea)
# print(trian_getperim)
