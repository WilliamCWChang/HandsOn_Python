from ctypes import *
print("=========================")
print("C Structure")
print("=========================")
print('\n\n')

#Structure is ctypes
class POINT(Structure):
	_fields_ = [("x", c_int), ("y", c_int)]

point = POINT(2,5)
print (">>point.x = {0}, point.y = {1}\n".format(point.x,point.y))

point = POINT(y=5) #reset y num
print (">>point.x = {0}, point.y = {1}\n".format(point.x,point.y))

POINT_ARRAY = POINT * 3

pa = POINT_ARRAY(POINT(7, 7), POINT(8, 8), POINT(9, 9))

for p in pa:
	print (p.x, p.y)
