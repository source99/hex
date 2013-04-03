import hex_class

hex_functions_debug = 0

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
	if hex_functions_debug > 0:   
		print "swapping points"
	temp = point1
	point1 = point2
	point2 = temp
	return point1, point2

#both corners across	

def distance_c0q2ob0(point1, point2):
#distance between 2 points in the same quadrant
#0 points on a corner
#2 points on a quadrant
#offset between points is 0
	
	if hex_functions_debug > 0:
		print "IN c0q2_ob0 "
	if point1.level > point2.level:
		point1, point2 = swap_points(point1, point2)        
	if hex_functions_debug > 0:   
		print_details(point1)
		print_details(point2)
	if point1.left_offset == point2.left_offset:
		return abs(point1.level - point2.level)
        if point1.level == point2.level:
                return abs(point1.left_offset - point2.left_offset)
        delta_levels = point2.level - point1.level
        delta_offsets = point2.left_offset - point1.left_offset
        if point1.left_offset > point2.left_offset:
            return point2.level - point1.level + point1.left_offset - point2.left_offset
        if delta_offsets > delta_levels:
            return delta_offsets
        else:
            return point2.level - point1.level
                    
	return -1


def distance_c1q1ob1(point1, point2):
#distance between a corner point and neighboring quadrant point.
#1 point is on a corner
#1 point is on a quadrant
#corner and quadrant are offset by 1
	if hex_functions_debug > 0:   
	  print "IN c1q1ob1: " + str(point1.point) + ", " + str(point2.point)
	  print_details(point1)
	  print_details(point2)
	  #same level
	if point1.is_corner and point1.level == point2.level:
		return point2.right_offset
	if point2.is_corner and point1.level == point2.level:
		return point1.left_offset
	
	if point1.is_corner and point1.level > point2.level:
		if hex_functions_debug > 0:   
			print "A creating new point: " + str(point1.point-1)
		temp_point = hex_class.full_point(point1.point-1)
		return 1 + distance_c0q2ob0(temp_point, point2)
	if point1.is_corner and point1.level < point2.level:
		if point2.right_offset > point2.level - point1.level:
			return point2.right_offset
		else:
			return point2.level - point1.level
	if point2.is_corner and point1.level < point2.level:
		if hex_functions_debug > 0:   
			print "B creating new point: " + str(point2.point+1)
		temp_point = hex_class.full_point(1)
		temp_point.left_offset = 1
		temp_point.right_offset = point2.level - 1
		temp_point.level = point2.level
		return 1 + distance_c0q2ob0(point1, temp_point)
	if point2.is_corner and point1.level > point2.level:
		if point1.left_offset > point1.level - point2.level:
			return point1.left_offset
		else:
			return point1.level - point2.level
	return -1

def distance_c2q0ob1(point1, point2):
#distance between 2 points both on a corner offset by 1
#2 points on corners
#0 points on quadrant
#corners are offset by 1

	if hex_functions_debug > 0:   
		print "IN c2q0ob1"
	return max(point1.level, point2.level)
        

def same_numbers(point1, point2):
#checks if both points are the same number
	if point1.point == point2.point:
		return True
	else:
		return False


def get_distance_ints(i, j):
	point1 = hex_class.full_point(i)
	point2 = hex_class.full_point(j)
	return get_distance(point1, point2)
	

def get_distance(point1, point2):
#super function that calculates the distance between any 2 points	
#first checks relationship between the 2 points and then calls the corresponding code


###Same numbers
	if same_numbers(point1, point2):
		if hex_functions_debug > 0:   
		  print "found identical numbers"
		return 0

###both center square	
	if both_center_square(point1, point2):
		if hex_functions_debug > 0:   
			print "found both_center_square"
		return 0

###one point is the center square	
	if one_center_square(point1, point2):
		if hex_functions_debug > 0:   
			print "found one_center_square"
		return max(point1.level, point2.level)

###organize points so point 1 is always to the left of point2
###this aids in simplifying many equations
	point1, point2 = point1_on_left(point1, point2)




###both points are in quadrants and offset by 1 
	if no_corners_off_by_1(point1, point2):
		if hex_functions_debug > 0:   
			print "no_corners_off_by_1"
		if point1.level == point2.level:
			return point1.left_offset + point2.right_offset
		if point1.level < point2.level:
			temp_point = hex_class.full_point(1)
			temp_point.level = point1.level
			temp_point.corner = point1.quadrant
			temp_point.quadrant = -1
			temp_point.left_offset = 0
			temp_point.right_offset = 0
			temp_point.is_corner = True
			temp_point.is_quadrant = False
			return point1.left_offset + distance_c1q1ob1(temp_point, point2)
		else:
			temp_point1 = hex_class.full_point(1)
			temp_point1.point = point2.point
			temp_point1.level = point2.level
			temp_point1.left_offset = point2.right_offset
			temp_point1.right_offset = point2.left_offset
			temp_point1.is_corner = False
			temp_point1.is_quadrant = True
			temp_point1.quadrant = point1.quadrant

			temp_point2 = hex_class.full_point(1)
			temp_point2.point = point1.point
			temp_point2.level = point1.level
			temp_point2.left_offset = point1.right_offset
			temp_point2.right_offset = point1.left_offset
			temp_point2.is_corner = False
			temp_point2.is_quadrant = True
			temp_point2.quadrant = point2.quadrant
			return get_distance(temp_point1, temp_point2)
		return -1 
		
		
###both points are in quadrants and offset by 2				
	if no_corners_off_by_2(point1, point2):
		if hex_functions_debug > 0:   
			print "found no_corners_off_by_2" + " point1 = " + str(point1.point) + " point2 = " + str(point2.point)
		if point1.right_offset <= point2.left_offset: 
			new_point1 = hex_class.full_point(1)
			new_point1.quadrant = -1
			new_point1.corner = point2.quadrant + 1
			new_point1.is_corner = True
			new_point1.is_quadrant = False
			new_point1.left_offset = 0
			new_point1.right_offset = 0
			new_point1.level = point1.right_offset
			if new_point1.corner == 8:
				new_point1.corner = 2
			return point1.level + distance_c1q1ob1(new_point1, point2)
		else:
			new_point2 = hex_class.full_point(1)
			new_point2.quadrant = -1
			new_point2.corner = point1.quadrant
			new_point2.is_corner = True
			new_point2.is_quadrant = False
			new_point2.left_offset = 0
			new_point2.right_offset = 0
			new_point2.level = point2.left_offset
			return point2.level + distance_c1q1ob1(point1, new_point2)
		return -1		

###both points are in quadrants and offset by 3	
	if no_corners_off_by_3(point1, point2):
		if hex_functions_debug > 0:
			print "found no_corners_off_by_3"
		return point1.level + point2.level
		
###one point on corner, one point on quadrant, offset by 1
	if one_corner_one_quadrant_off_by_1(point1, point2):
		if hex_functions_debug > 0:
			print "found one_corner_one_quadrant_off_by_1"
		return distance_c1q1ob1(point1, point2)
	

###one point on corner, one point on quadrant, offset by 2	
	if one_corner_one_quadrant_off_by_2(point1, point2):
		if hex_functions_debug > 0:   
			print "found one_corner_one_quadrant_off_by_2_" 
			print point1.point, point2.point
			print "ORIG POINTS"
			print_details(point1)
			print_details(point2)
			print "END ORIG POINTS"

		if point1.is_corner:
			if point1.level <= point2.level:
				return point2.right_offset + max(point1.level, point2.left_offset)
			else:
				return point2.right_offset + max(point1.level, point2.left_offset)
		else:
			if hex_functions_debug > 0:   
				print "MAKING NEW POINT in one_corner_one_quadrant_off_by_2"
			temp_point1 = hex_class.full_point(1)
			temp_point1.point = point1.point
			temp_point1.quadrant = point2.corner - 2
			temp_point1.left_offset = point1.right_offset
			temp_point1.right_offset = point1.left_offset
			temp_point1.is_quadrant = True
			temp_point1.is_corner = False
			temp_point1.level = point1.level
			
			if temp_point1.quadrant == 1:
				temp_point1.quadrant = 7
			if temp_point1.quadrant == 0:
				temp_point1.quadrant = 6
			if hex_functions_debug > 0:   
				print "NEW POINTS"
				print_details(point2)
				print_details(temp_point1)
				print "END NEW POINTS"
			return get_distance(temp_point1, point2)
		return -1			

###one point on corner, one point on quadrant, offset by 3	
	if one_corner_one_quadrant_off_by_3(point1, point2):
		if hex_functions_debug > 0:   
			print "found one_corner_one_quadrant_off_by_3"
		return point1.level + point2.level
	
	
###both points in the same quadrant
	if no_corners_same_quadrant(point1, point2):
		if hex_functions_debug > 0:   
			print "found no_corners_same_quadrant"
		return distance_c0q2ob0(point1, point2)



###both points are on the same corner
	if both_corners_same_corner(point1, point2):
		if hex_functions_debug > 0:   
			print "found both_corners_same_corner"
		return abs(point1.level - point2.level)

###both points are on corners offset by 1
	if both_corners_off_by_1(point1, point2):
		if hex_functions_debug > 0:   
			print "found both_corners_off_by_1"
		return max(point1.level, point2.level)

###both points are on corners offset by 2
	if both_corners_off_by_2(point1, point2):
		if hex_functions_debug > 0:   
			print "found both_corners_off_by_2"
		return point1.level + point2.level
		
###both points are on corners offset by 3
	if both_corners_off_by_3(point1, point2):
		if hex_functions_debug > 0:   
			print "found both_corners_off_by_3"
		return point1.level + point2.level

###Should never get here
	return -1



def point1_on_left(point1, point2):
#make orientation so point 1 is always to the left of point2
#only need to check forward 3 corners/quadrants because all calculations
#can be done by moving forward 3 corners/quadrants
#if its more than 3 points forward then just move in the opposite direction 
#to find a shorter path

###TODO: Optimize code to use offset instead of checking every possible combination

	if point1.is_quadrant and point2.is_corner:
	
		if point1.quadrant == 2 and point2.corner == 3:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 2 and point2.corner == 4:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 2 and point2.corner == 5:
			point1, point2 = swap_points(point1, point2)
		
		if point1.quadrant == 3 and point2.corner == 4:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 3 and point2.corner == 5:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 3 and point2.corner == 6:
			point1, point2 = swap_points(point1, point2)
		
		if point1.quadrant == 4 and point2.corner == 5:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 4 and point2.corner == 6:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 4 and point2.corner == 7:
			point1, point2 = swap_points(point1, point2)
		
		if point1.quadrant == 5 and point2.corner == 6:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 5 and point2.corner == 7:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 5 and point2.corner == 2:
			point1, point2 = swap_points(point1, point2)
		
		if point1.quadrant == 6 and point2.corner == 7:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 6 and point2.corner == 2:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 6 and point2.corner == 3:
			point1, point2 = swap_points(point1, point2)
		
		if point1.quadrant == 7 and point2.corner == 2:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 7 and point2.corner == 3:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 7 and point2.corner == 4:
			point1, point2 = swap_points(point1, point2)
			
	if point1.is_corner and point2.is_quadrant:
	
		if point1.corner == 2 and point2.quadrant == 2:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 2 and point2.quadrant == 3:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 2 and point2.quadrant == 4:
			point1, point2 = swap_points(point1, point2)

		if point1.corner == 3 and point2.quadrant == 3:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 3 and point2.quadrant == 4:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 3 and point2.quadrant == 5:
			point1, point2 = swap_points(point1, point2)

		if point1.corner == 4 and point2.quadrant == 4:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 4 and point2.quadrant == 5:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 4 and point2.quadrant == 6:
			point1, point2 = swap_points(point1, point2)
		
		if point1.corner == 5 and point2.quadrant == 5:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 5 and point2.quadrant == 6:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 5 and point2.quadrant == 7:
			point1, point2 = swap_points(point1, point2)

		if point1.corner == 6 and point2.quadrant == 6:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 6 and point2.quadrant == 7:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 6 and point2.quadrant == 2:
			point1, point2 = swap_points(point1, point2)
						
		if point1.corner == 7 and point2.quadrant == 7:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 7 and point2.quadrant == 2:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 7 and point2.quadrant == 3:
			point1, point2 = swap_points(point1, point2)
						
	if point1.is_quadrant and point2.is_quadrant:

		if point1.quadrant == 2 and point2.quadrant == 3:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 2 and point2.quadrant == 4:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 2 and point2.quadrant == 5:
			point1, point2 = swap_points(point1, point2)

		if point1.quadrant == 3 and point2.quadrant == 4:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 3 and point2.quadrant == 5:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 3 and point2.quadrant == 6:
			point1, point2 = swap_points(point1, point2)

		if point1.quadrant == 4 and point2.quadrant == 5:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 4 and point2.quadrant == 6:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 4 and point2.quadrant == 7:
			point1, point2 = swap_points(point1, point2)

		if point1.quadrant == 5 and point2.quadrant == 6:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 5 and point2.quadrant == 7:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 5 and point2.quadrant == 2:
			point1, point2 = swap_points(point1, point2)

		if point1.quadrant == 6 and point2.quadrant == 7:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 6 and point2.quadrant == 2:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 6 and point2.quadrant == 3:
			point1, point2 = swap_points(point1, point2)
								
		if point1.quadrant == 7 and point2.quadrant == 2:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 7 and point2.quadrant == 3:
			point1, point2 = swap_points(point1, point2)
		if point1.quadrant == 7 and point2.quadrant == 4:
			point1, point2 = swap_points(point1, point2)
			
			
	if point1.is_corner and point2.is_corner:
		
		if point1.corner == 2 and point2.corner == 3:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 2 and point2.corner == 4:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 2 and point2.corner == 5:
			point1, point2 = swap_points(point1, point2)

		if point1.corner == 3 and point2.corner == 4:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 3 and point2.corner == 5:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 3 and point2.corner == 6:
			point1, point2 = swap_points(point1, point2)
								
		if point1.corner == 4 and point2.corner == 5:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 4 and point2.corner == 6:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 4 and point2.corner == 7:
			point1, point2 = swap_points(point1, point2)
								
		if point1.corner == 5 and point2.corner == 6:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 5 and point2.corner == 7:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 5 and point2.corner == 2:
			point1, point2 = swap_points(point1, point2)

		if point1.corner == 6 and point2.corner == 7:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 6 and point2.corner == 2:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 6 and point2.corner == 3:
			point1, point2 = swap_points(point1, point2)
								
		if point1.corner == 7 and point2.corner == 2:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 7 and point2.corner == 3:
			point1, point2 = swap_points(point1, point2)
		if point1.corner == 7 and point2.corner == 4:
			point1, point2 = swap_points(point1, point2)
	return point1, point2								
