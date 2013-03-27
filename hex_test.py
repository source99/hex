import hex as hex
import sys


point = int(sys.argv[1])


if (hex.get_level(0) != 0):
	print "failed level test with get_level(0)"
	exit()
if (hex.get_level(1) != 1):
	print "failed level test with get_level(1)"
	exit()
if (hex.get_level(9) != 2):
	print "failed level test with get_level(9)"
	exit()
if (hex.get_level(127) != 6):
	print "failed level test with get_level(127)"
	exit()
if (hex.get_level(128) != 7):
	print "failed level test with get_level(128)"
	exit()
	
	
#corner 7 tests
if (hex.is_corner(7)!= 7):	
	print "failed is_corner test with is_corner(7)"
	exit()
if (hex.is_corner(8)!=-1):	
	print "failed is_corner test with is_corner(8)"
	exit()
if (hex.is_corner(20)!=-1):	
	print "failed is_corner test with is_corner(20)"
	exit()
if (hex.is_corner(38)!=-1):	
	print "failed is_corner test with is_corner(38)"
	exit()
if (hex.is_corner(60)!=-1):	
	print "failed is_corner test with is_corner(60)"
	exit()
if (hex.is_corner(61)!=7):	
	print "failed is_corner test with is_corner(61)"
	exit()
	
#corner 2 tests
if (hex.is_corner(6)!=6):	
	print "failed is_corner test with is_corner(6)"
	exit()
if (hex.is_corner(10)!=-1):	
	print "failed is_corner test with is_corner(10)"
	exit()
if (hex.is_corner(55)!=-1):	
	print "failed is_corner test with is_corner(55)"
	exit()
if (hex.is_corner(66)!=2):	
	print "failed is_corner test with is_corner(66)"
	exit()
	
	
	
#get_quadrant tests

if(hex.get_quadrant(8)!=7):
	print "failed get_quadrant(8)"
	exit()	
if(hex.get_quadrant(10)!=2):
	print "failed get_quadrant(10)"
	exit()	
if(hex.get_quadrant(12)!=3):
	print "failed get_quadrant(1)"
	exit()	
if(hex.get_quadrant(14)!=4):
	print "failed get_quadrant(14)"
	exit()		
if(hex.get_quadrant(16)!=5):
	print "failed get_quadrant(16)"
	exit()	
if(hex.get_quadrant(18)!=6):
	print "failed get_quadrant(18)"
	exit()	
if(hex.get_quadrant(20)!=7):
	print "failed get_quadrant(20)"
	exit()	
if(hex.get_quadrant(67)!=2):
	print "failed get_quadrant(67)"
	exit()	
if(hex.get_quadrant(45)!=0):
	print "failed get_quadrant(45)"
	exit()	


def test_full(point1, point2, correct_distance):
	print "Testing: " + str(point1) + ", " + str(point2) + ", " + str(correct_distance)
	p1, p2, distance = hex.get_distance(point1, point2)
	print "Result: " + str(distance)
	if distance != correct_distance:
		print "Failed"
		print point1, point2, distance
		print "correct distance = " + str(correct_distance)
		exit()
	temp = point1
	point1 = point2
	point2 = temp
	print "Testing: " + str(point1) + ", " + str(point2) + ", " + str(correct_distance)
	p1, p2, distance = hex.get_distance(point1, point2)
	print "Result: " + str(distance)
	if distance != correct_distance:
		print "Failed"
		print point1, point2, distance
		print "correct distance = " + str(correct_distance)
		exit()
	return	

	
test_full	(70,99,3)
test_full	(10,99,4)
#test_full	(10,99,5)
test_full	(10,100,4)
test_full	(2,22,2)
test_full	(9,71,5)
test_full	(9,23,1)
test_full	(9,101,4)
test_full	(97,68,3)
test_full	(97,44,5)
test_full	(97,70,5)
	
	
	
	
	
	
print "PASSED ALL TESTS"	