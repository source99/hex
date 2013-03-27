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
	for line in fp:
		print line
		i,j,correct_distance = line.split(", ")
		i = int(i)
		j = int(j)
		point1 = hex_class.full_point(i)
		point2 = hex_class.full_point(j)
		correct_distance = int(correct_distance)
		if hex_functions.both_center_square(point1,point2) or hex_functions.one_center_square(point1, point2) or hex_functions.no_corners_same_quadrant(point1, point2) or hex_functions.one_corner_one_quadrant_off_by_1(point1, point2):
			calculated_distance = hex_functions.get_distance(point1,point2)
			if calculated_distance != correct_distance:
				print "failed get_distance(" + str(i) + "," + str(j) + ")"
				print "returned " + str(calculated_distance) + "."
				print "correct  " + str(correct_distance)
				hex_functions.print_details(point1)
				hex_functions.print_details(point2)
				exit()
	fp.close()
	print "ALL TESTS PASSED"
	test_range_1_solution()
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
			if found == 0 or found > 1:
				hex_functions.print_details(point1)
				hex_functions.print_details(point2)
	
				print "failed " + str(i) + ", " + str(j)
				print "found = " + str(found)
				return -1
	return 1		
		
test_specifics()
