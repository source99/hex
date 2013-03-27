import sys
import hex_class
import hex_functions

def test_class_functions(num1, num2):
	point1 = hex_class.full_point(num1)
	point2 = hex_class.full_point(num2)
	if hex_functions.no_corners_same_quadrant(point1, point2):
		print "no corners same quadrant"
	if hex_functions.no_corners_neighbor_quadrants(point1, point2):
		print "no corners and neighbor quadrants"
	return
	
	
num1 = 63
num2 = 69
if hex_functions.no_corners_same_quadrant(hex_class.full_point(num1), hex_class.full_point(num2)):
	print "FAILED 63, 69, no_corners_same_quadrant"
	exit()
	
num1 = 63
num2 = 69
if not hex_functions.no_corners_neighbor_quadrants(hex_class.full_point(num1), hex_class.full_point(num2)):
	print "FAILED 63, 69, no_corners_same_quadrant"
	exit()
	
	
	
	
	
	
print 63, 69	
test_class_functions(63,69)
print 69, 63
test_class_functions(69,63)
print 69, 100
test_class_functions(69,100)
print 69, 100
test_class_functions(100,69)
print 63, 69	
test_class_functions(63,69)
