import hex_class

#####################################
#General Functions
#####################################

def print_details(point):
	print "POINT DETAILS"
	print "point = " + str(point.point)
	print "level = " + str(point.level)
	print "corner = " + str(point.corner)
	print "quadrant = " + str(point.quadrant)
	print "is_corner = " + str(point.is_corner)
	print "is_quadrant = " + str(point.is_quadrant)
	print "left_offset = " + str(point.left_offset)
	print "right_offset = " + str(point.right_offset)
	print "\n"

def digit_one_off(digit1, digit2):
	if digit1 == digit2:
		return False
	if digit1 + 1 == digit2:
		return True
	if digit1 == digit2 + 1:
		return True
	if digit1 == 2 and digit2 == 7:
		return True
	if digit1 == 7 and digit2 == 2:
		return True
	return False
	
def digit_two_off(digit1, digit2):
	if digit1 == digit2 + 2:
		return True
	if digit2 == digit1 + 2:
		return True
	if digit1 == 7 and digit2 == 3:
		return True
	if digit1 == 3 and digit2 == 7:
		return True
	if digit1 == 6 and digit2 == 2:
		return True
	if digit1 == 2 and digit2 == 6:
		return True
	return False

def digit_three_off(digit1, digit2):
	if digit1 == digit2+3:
		return True
	if digit2 == digit1 + 3:
		return True
	if digit1 == 4 and digit2 == 7:
		return True
	if digit2 == 4 and digit1 == 7:
		return True
	return False

#####################################
#General Functions END
#####################################

#####################################
#UNIQUE FUNCTIONS
#####################################

def one_center_square(point1, point2):
	if point1.level == 0 and point2.level != 0:
		return True
	if point2.level == 0 and point1.level != 0:
		return True
	return False
	
	
def both_center_square(point1, point2):
	if point1.level == 0 and point2.level == 0:
		return True
	return False
	
	

#####################################
#UNIQUE FUNCTIONS END
#####################################


#####################################
#NO CORNERS
#####################################

def no_corners_same_quadrant(point1, point2):
	if point1.is_quadrant and point2.is_quadrant and point1.quadrant == point2.quadrant:
		return True
	else:
		return False			

def no_corners_off_by_1(point1, point2):
	if point1.is_quadrant and point2.is_quadrant and digit_one_off(point1.quadrant, point2.quadrant):
		return True
	else:
		return False			
		
def no_corners_off_by_2(point1, point2):
	if point1.is_quadrant and point2.is_quadrant:
		if digit_two_off(point1.quadrant, point2.quadrant):
			return True
	return False
	
def no_corners_off_by_3(point1, point2):
	if point1.is_quadrant and point2.is_quadrant:
		if digit_three_off(point1.quadrant, point2.quadrant):
			return True
	return False		

#####################################
#NO CORNERS END
#####################################

	
#####################################
#ONE CORNER ONE QUADRANT
#####################################
	
def one_corner_one_quadrant_off_by_1(point1, point2):
	if point1.level == 0 or point2.level == 0:
		return False
	if point1.is_corner and point2.is_quadrant:
		if (point1.corner == point2.quadrant) or (point1.corner == 2 and point2.quadrant == 7):
			return True
	if point2.is_corner and point1.is_quadrant:
		if (point2.corner == point1.quadrant) or (point2.corner == 2 and point1.quadrant == 7):
			return True
	return False
	
	
def one_corner_one_quadrant_off_by_2(point1, point2):
	if point1.level == 0 or point2.level == 0:
		return False
	if point1.is_corner and point2.is_quadrant:
		if (point1.corner == point2.quadrant + 1) or (point1.corner == 2 and point2.quadrant == 6)or (point1.corner == 3 and point2.quadrant == 7):
			return True
		if (point1.corner + 1 == point2.quadrant) or (point1.corner == 6 and point2.quadrant == 2)or (point1.corner == 7 and point2.quadrant == 3):
			return True
	if point2.is_corner and point1.is_quadrant:
		if (point2.corner == point1.quadrant + 1) or (point2.corner == 2 and point1.quadrant == 6) or (point2.corner == 3 and point1.quadrant == 7):
			return True
		if (point2.corner + 1 == point1.quadrant) or (point2.corner == 6 and point1.quadrant == 2) or (point2.corner == 3 and point1.quadrant == 7):
			return True
	return False
	
def one_corner_one_quadrant_off_by_3(point1, point2):
	if point1.level == 0 or point2.level == 0:
		return False
	if point1.is_corner and point2.is_quadrant:
		if (point1.corner == point2.quadrant + 2) or (point1.corner == 2 and point2.quadrant == 5):
			return True
		if (point1.corner + 3 == point2.quadrant) or (point1.corner == 5 and point2.quadrant == 2):
			return True
	if point2.is_corner and point1.is_quadrant:
		if (point2.corner == point1.quadrant + 2) or (point2.corner == 2 and point1.quadrant == 5):
			return True
		if (point2.corner + 3 == point1.quadrant) or (point2.corner == 5 and point1.quadrant == 2):
			return True
	return False
	
			
#####################################
#ONE CORNER ONE QUADRANT END
#####################################


#####################################
#BOTH CORNERS
#####################################
	
def both_corners_same_corner(point1, point2):
	if point1.level == 0 or point2.level == 0:
		return False
	if point1.is_corner and point2.is_corner and point1.corner == point2.corner:
		return True
	return False
	
#both corners neighboring
def both_corners_off_by_1(point1, point2):
	if point1.level == 0 or point2.level == 0:
		return False
	if point1.is_corner and point2.is_corner and digit_one_off(point1.corner, point2.corner):
		return True
	return False

def both_corners_off_by_2(point1, point2):
	if point1.level == 0 or point2.level == 0:
		return False
	if point1.is_corner and point2.is_corner and digit_two_off(point1.corner, point2.corner):
		return True
	return False

def both_corners_off_by_3(point1, point2):
	if point1.level == 0 or point2.level == 0:
		return False
	if point1.is_corner and point2.is_corner and digit_three_off(point1.corner, point2.corner):
		return True
	return False
	
#####################################
#BOTH CORNERS END
#####################################

#both corners across	


def get_distance(point1, point2):
	if both_center_square(point1, point2):
		print "found both_center_square"
		return 0

	if one_center_square(point1, point2):
		print "found one_center_square"
		return max(point1.level, point2.level)

	if no_corners_same_quadrant(point1, point2):
		print "found no_corners_same_quadrant"
		if point1.level == point2.level:
			return abs(point1.point - point2.point)
		if point1.level > point2.level:
			if point1.left_offset == point2.left_offset:
				return point1.level - point2.level
			if point1.left_offset > point2.left_offset:
				return point1.left_offset - point2.left_offset
			if point1.left_offset < point2.left_offset:
				return (point1.level - point2.level) + (point2.left_offset - point1.left_offset)
		else: #point2.level > point1.level
			if point2.left_offset == point1.left_offset:
				return point2.level - point1.level
			if point2.left_offset > point1.left_offset:
				return point2.left_offset - point1.left_offset
			if point2.left_offset < point1.left_offset:
				return (point2.level - point1.level) + (point1.left_offset - point2.left_offset)
			
			
			
		print "NEED CALCULATION"
	if no_corners_off_by_1(point1, point2):
		print "found no_corners_off_by_1"
		
		print "NEED CALCULATION"
	if no_corners_off_by_2(point1, point2):
		print "found no_corners_off_by_2"
		print "NEED CALCULATION"
	if no_corners_off_by_3(point1, point2):
		print "found no_corners_off_by_3"
		print "NEED CALCULATION"
	
	if one_corner_one_quadrant_off_by_1(point1, point2):
		print "found one_corner_one_quadrant_off_by_1"
		#make sure point1 is always the corner
		if point1.is_quadrant:
			temp = point1
			point1 = point2
			point2 = temp
		#same level
		if point1.level == point2.level:
			if point1.point > point2.point:
				return point2.right_offset
			else:
				return point2.left_offset
		#corner is higher	
		if point1.level > point2.level:
			if point1.corner == point2.quadrant:
				return point2.left_offset + (point1.level - point2.level)
			else:
				return point2.right_offset + (point1.level - point2.level)				
		#corner is lower
		if point2.level > point1.level:
			if (point2.level - point1.level) <= point2.right_offset:
				return point2.right_offset
			if (point2.level - point1.level) > point2.right_offset:	
				return point2.level - point2.right_offset + (point2.level - point2.right_offset) - point1.level				


	if one_corner_one_quadrant_off_by_2(point1, point2):
		print "found one_corner_one_quadrant_off_by_2"
		print "NEED CALCULATION"
	if one_corner_one_quadrant_off_by_3(point1, point2):
		print "found one_corner_one_quadrant_off_by_3"
		print "NEED CALCULATION"
	
	if both_corners_same_corner(point1, point2):
		print "found both_corners_same_corner"
		print "NEED CALCULATION"
	if both_corners_off_by_1(point1, point2):
		print "found both_corners_off_by_1"
		print "NEED CALCULATION"
	if both_corners_off_by_2(point1, point2):
		print "found both_corners_off_by_2"
		print "NEED CALCULATION"
	if both_corners_off_by_3(point1, point2):
		print "found both_corners_off_by_3"
		print "NEED CALCULATION"



	return -1