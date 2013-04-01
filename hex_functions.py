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
		if ((point1.corner) % 6 == point2.quadrant % 6) or (point1.corner % 6 == (point2.quadrant + 1) % 6):
			return True
	if point2.is_corner and point1.is_quadrant:
		if ((point2.corner) % 6 == point1.quadrant % 6) or (point2.corner % 6 == (point1.quadrant + 1) % 6):
			return True
	return False
	
	
def one_corner_one_quadrant_off_by_2(point1, point2):
	if point1.level == 0 or point2.level == 0:
		return False
	if point1.is_corner and point2.is_quadrant:
		if ((point1.corner + 1) % 6 == point2.quadrant % 6) or (point1.corner % 6 == (point2.quadrant + 2) % 6):
			return True
	if point2.is_corner and point1.is_quadrant:
		if ((point2.corner + 1) % 6 == point1.quadrant % 6) or (point2.corner % 6 == (point1.quadrant + 2) % 6):
			return True
	return False
	
def one_corner_one_quadrant_off_by_3(point1, point2):
	if point1.level == 0 or point2.level == 0:
		return False
	if point1.is_corner and point2.is_quadrant:
		if ((point1.corner + 2) % 6 == point2.quadrant % 6) or (point1.corner % 6 == (point2.quadrant + 3) % 6):
			return True
	if point2.is_corner and point1.is_quadrant:
		if ((point2.corner + 2) % 6 == point1.quadrant % 6) or (point2.corner % 6 == (point1.quadrant + 3) % 6):
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

def swap_points(point1, point2):
    print "swapping points"
    temp = point1
    point1 = point2
    point2 = temp
    return point1, point2

#both corners across	

def distance_c0q2ob0(point1, point2):
        print "IN c0q2_ob0"
        print_details(point1)
        print_details(point2)        
        if point2.left_offset <= point1.left_offset - abs(point1.level - point2.level):
            print "A"
            return abs(point1.left_offset - point2.left_offset) + abs(point1.level - point2.level)
        print "B"
	return max(abs(point1.level - point2.level), abs(point1.left_offset - point2.left_offset))


def distance_c1q1ob1(point1, point2):
        if (point1.is_quadrant and ((point1.quadrant < point2.corner) or \
            (point1.quadrant ==7 and point2.corner == 2)) or \
            (point1.is_corner and ((point1.corner == point2.quadrant) or \
            point1.corner == 7 and point2.quadrant == 7))):
            print "swapping points to keep point 1 to the left"
            point1, point2, = swap_points(point1, point2)
        #force it so point1 is always the quadrant and always to the left of the corner
        if not point1.is_quadrant:
            print "creating new point so point1 is always quadrant"
            temp_point1 = hex_class.full_point(1)
            temp_point1.level = point2.level
            temp_point1.right_offset = point2.left_offset
            temp_point1.left_offset = point2.right_offset
            point2 = point1
        else:
            temp_point1 = point1
        if temp_point1.level == point2.level:
            return point1.left_offset
        else:
            return distance_c0q2ob0(temp_point1, point2)

def distance_c2q0ob1(point1, point2):
        return max(point1.level, point2.level)
        

def get_distance(point1, point2):
        if point1.point == point2.point:
            print "found identical numbers"
            return 0
	if both_center_square(point1, point2):
		print "found both_center_square"
		return 0

	if one_center_square(point1, point2):
		print "found one_center_square"
		return max(point1.level, point2.level)

	if no_corners_same_quadrant(point1, point2):
                print "found no_corners_same_quadrant"
                if (point1.level > point2.level):
                    point1, point2 = swap_points(point1, point2)
                return distance_c0q2ob0(point1, point2)

	if no_corners_off_by_1(point1, point2):
                return -1
				
	if no_corners_off_by_2(point1, point2):
                return -1

	if no_corners_off_by_3(point1, point2):
                return -1
	
	if one_corner_one_quadrant_off_by_1(point1, point2):
            return distance_c1q1ob1(point1, point2)


	if one_corner_one_quadrant_off_by_2(point1, point2):
		print "found one_corner_one_quadrant_off_by_2"
                if point1.is_quadrant:
                    if point1.level >= point2.level:
                         return point2.level + distance_c0q2ob0(point1, point2)
                    if point1.level < point2.level:
                         return point1.left_offset + distance_c2q0ob1(point1, point2)
                else:
                    print "B"
                    if point2.level >= point1.level:
                        print "C" 
                        return point1.level + distance_c0q2ob0(point2, point1)
                    if point2.level < point1.level:
                         print "D"
                         return point2.left_offset + distance_c2q0ob1(point2, point1)
                
                return -1
	if one_corner_one_quadrant_off_by_3(point1, point2):
		print "found one_corner_one_quadrant_off_by_3"
		print "NEED CALCULATION"
                return -1
	
	if both_corners_same_corner(point1, point2):
		print "found both_corners_same_corner"
		print "NEED CALCULATION"
                return -1
	if both_corners_off_by_1(point1, point2):
		print "found both_corners_off_by_1"
		print "NEED CALCULATION"
                return -1
	if both_corners_off_by_2(point1, point2):
		print "found both_corners_off_by_2"
		print "NEED CALCULATION"
                return -1
	if both_corners_off_by_3(point1, point2):
		print "found both_corners_off_by_3"
		print "NEED CALCULATION"
                return -1



	return -1
