import sys
import hex_class
import hex_functions

def test_specifics():

#test_points = [1,2,3,4,5,6,7,8,10,12,17,16,18,92,96,97,98,102,103,104,108,109,110,114,115,116,120,121,122,126,127,92,43,47,51,55,59,39]
#	test_points = [1,97,43,102,47,114,55,125,62]
	
#	for i in test_points:
#		for j in test_points:
#			print str(i) + ", " + str(j) + ", A"

	fp = open("test.csv", "r")
	passed = 0
	tests = 0
	
	for line in fp:
		if line[0] == "#":
			print "skipping " + line
		else:
			tests+=2
			print "START input = " + line
			i,j,correct_distance = line.split(", ")
			i = int(i)
			j = int(j)
			if i == 0 and j == 0:
				exit()
			point1 = hex_class.full_point(i)
			point2 = hex_class.full_point(j)
			correct_distance = int(correct_distance)
			calculated_distance1 = hex_functions.get_distance(point1,point2)
	#		calculated_distance2 = calculated_distance1
			calculated_distance2 = hex_functions.get_distance(point2,point1)
			if calculated_distance1 != correct_distance or calculated_distance2 != correct_distance:
				print "input = " + line
				print "failed get_distance(" + str(i) + "," + str(j) + ")"
				print "returned " + str(calculated_distance1) + "."
				print "correct  " + str(correct_distance)
				hex_functions.print_details(point1)
				hex_functions.print_details(point2)
				exit()
			else:
	#			print "PASSED " + line
				passed +=2
	fp.close()
	print "ALL TESTS PASSED"
	print "total tests = " + str(tests)
	print "tests passed = " + str(passed)
	return


def test_range_1_solution():

	for i in range(1, 100):
		for j in range(1,100):
			found = 0
			point1 = hex_class.full_point(i)
			point2 = hex_class.full_point(j)
			print "\n\n "
			print i,j
	
			if hex_functions.both_center_square(point1, point2):
				print "found both_center_square"
				found+=1
	
			if hex_functions.one_center_square(point1, point2):
				print "found one_center_square"
				found+=1
	
			if hex_functions.no_corners_off_by_1(point1, point2):
				print "found no_corners_off_by_1"
				found+=1
			if hex_functions.no_corners_same_quadrant(point1, point2):
				print "found no_corners_same_quadrant"
				found+=1
			if hex_functions.no_corners_off_by_2(point1, point2):
				print "found no_corners_off_by_2"
				found+=1
			if hex_functions.no_corners_off_by_3(point1, point2):
				print "found no_corners_off_by_3"
				found+=1
			
			if hex_functions.one_corner_one_quadrant_off_by_1(point1, point2):
				print "found one_corner_one_quadrant_off_by_1"
				found+=1
			if hex_functions.one_corner_one_quadrant_off_by_2(point1, point2):
				print "found one_corner_one_quadrant_off_by_2"
				found+=1
			if hex_functions.one_corner_one_quadrant_off_by_3(point1, point2):
				print "found one_corner_one_quadrant_off_by_3"
				found+=1
			
			if hex_functions.both_corners_same_corner(point1, point2):
				print "found both_corners_same_corner"
				found+=1
			if hex_functions.both_corners_off_by_1(point1, point2):
				print "found both_corners_off_by_1"
				found+=1
			if hex_functions.both_corners_off_by_2(point1, point2):
				print "found both_corners_off_by_2"
				found+=1
			if hex_functions.both_corners_off_by_3(point1, point2):
				print "found both_corners_off_by_3"
				found+=1
			if found != 1:
				hex_functions.print_details(point1)
				hex_functions.print_details(point2)
	
				print "failed " + str(i) + ", " + str(j)
				print "found = " + str(found)
				return -1
	return 1		
		
def interactive_mode():
	while True:
		input = raw_input("Enter 2 positive numbers to return shortest path.  Enter '0 0' to exit\n")
		print input
		i, j = input.split(" ")
		i = int(i)
		j = int(j)
		if i == 0 and j == 0:
			break
		point1 = hex_class.full_point(i)
		point2 = hex_class.full_point(j)
		distance = hex_functions.get_distance(point1,point2)
		print "distance between these two points is " + str(distance)
	return 1
			






#testing functions
#interactive_mode()
test_specifics()
#test_range_1_solution()
