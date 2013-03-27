import sys

'''
Hex graph algorithm
	determine quadrants
	determine directions to move
	move each direction until points match
'''

debug = 0


def usage():
	print "hex.py point1, point2, [max_node]"
	print "point1 and point2 must be positive integers to return shortest path"
	print "if point1 == 0 and point2 == 0 then Program will exit"
	return

def level_quadrant_corner(point):
	corner = is_corner(point)
	quadrant = get_quadrant(point)
	level = get_level(point)
	if corner > 0:
		level_offset = 0
	else:
		level_offset = get_level_offset(quadrant, level, point)
	return level, quadrant, corner, level_offset

def get_level_offset(quadrant, level, point):
#function should not be called when input point is a corner
	level = float(level)
	if quadrant == 7:
		level -= 1
	first_corner = ((((level-1) / 2) + 0.5) * (level-1)) * 6 + 2 + level-1	
	quadrant_corner = first_corner + (quadrant-2) * (level)
	level_offset = point - quadrant_corner
	if debug > 0:
		print "level = " + str(level)
		print "quadrant = " + str(quadrant)
		print "first corner = " + str(first_corner)
		print "quadrant corner = " + str(quadrant_corner)
		print "level_offset = " + str(level_offset)
	return level_offset

	return 0
def get_quadrant(point):
#input = 	point:positive integer
#output = quadrant of that point
#quadrant is defined as a number between corners n and n +1.
#the returned quadrant is one section clockwise from the corner
#point:quadrant
#8:7
#77:4
	if debug > 0:
		print "input to get_quadrant = " + str(point)
	if point <= 7:
		return 0
	if is_corner(point) > 0:
		if debug > 0:
			print "corner found"
		return 0
	
	level = get_level(point)
	index = float(level)
	corner_2 = ((((index-1) / 2) + 0.5) * (index-1)) * 6 + 2 + index-1
	corner_3 = corner_2 + index
	corner_4 = corner_3 + index
	corner_5 = corner_4 + index
	corner_6 = corner_5 + index
	corner_7 = corner_6 + index

	if debug > 0:
		print "corner_2 = " + str(corner_2)
		print "corner_3 = " + str(corner_3)
		print "corner_4 = " + str(corner_4)
		print "corner_5 = " + str(corner_5)
		print "corner_6 = " + str(corner_6)
		print "corner_7 = " + str(corner_7)

	if point < corner_2: 
		return 7
	if point < corner_3: 
		return 2
	if point < corner_4: 
		return 3
	if point < corner_5: 
		return 4
	if point < corner_6: 
		return 5
	if point < corner_7: 
		return 6

	return quadrant

def get_level(point):
#input = point:positive integer
#returns the level of that point.  Level is defined as number of complete circles of digit: >= 0
#point:level
#1:0
#2-7:1
#8-19:2
#20:37:3
	global debug
	index = float(1)
	if point == 0:
		return 0
	if point <=7:
		return 1
	while point >= (((index / 2) + 0.5) * index) * 6 + 2:
		index +=1		
	if debug > 1:
		print "level of " + str(point) + " is " + str(index)
	return int(index)

def is_corner(point):
#input = point:positive integer
#output = whether or not that point is on a corner line
#point:is_corner
#1:1
#37:7
#36:-1 	
	if debug > 1:
		print "input to is_corner = " + str(point)
	level = get_level(point)
	if point == 0:
		return 0
	if point <= 7:
		return point
	index = float(level)
	corner_2 = ((((index-1) / 2) + 0.5) * (index-1)) * 6 + 2 + index-1
	corner_3 = corner_2 + index
	corner_4 = corner_3 + index
	corner_5 = corner_4 + index
	corner_6 = corner_5 + index
	corner_7 = corner_6 + index
	if debug > 1:
		print "level is = " + str(level)
		print "corner_2 = " + str(corner_2)
		print "corner_3 = " + str(corner_3)
		print "corner_4 = " + str(corner_4)
		print "corner_5 = " + str(corner_5)
		print "corner_6 = " + str(corner_6)
		print "corner_7 = " + str(corner_7)
	if point == corner_2:
		return 2
	if point == corner_3:
		return 3
	if point == corner_4:
		return 4
	if point == corner_5:
		return 5
	if point == corner_6:
		return 6
	if point == corner_7:
		return 7
		

	
	return -1

def get_angles(quadrant_1, quadrant_2):
	angles_1 = [0,0,0,0,0,0]
	angles_2 = [0,0,0,0,0,0]
	
	
	
	return angles_1, angles_2

def check_args(point1, point2):
#exit if both are 0
#check to make sure both points are positive integers
#go to usage if they are invalid
	if point1 == "0" and point2 == "0":
		print "Goodby"
		exit()
	if point1[:0] == "-" or point2[:0] == "-":
		usage()
		exit(-1)
	if point1.isdigit() and point2.isdigit():
		return True
	usage()
	exit(-1)
	return False	
	
def print_result(point1, point2, distance):
	print "\n\n\nDistance between " + str(point1) + " and " + str(point2) + " is " + str(distance)
	exit()
	return
	
def distance_both_corners(point1, point2):
		print "both corners"
		level1, quadrant1, corner1, level_offset1 = level_quadrant_corner(point1)
		level2, quadrant2, corner2, level_offset2 = level_quadrant_corner(point2)
		print "corner1 = " + str(corner1)
		print "corner2 = " + str(corner2)
		if corner1 == 0:
			print "center point"
			return point1, point2, level2
		if corner1 == corner2:
			print "same corner"
			distance = level2 - level1
			return point1, point2, distance
		if ((corner1 + 1) % 6) == (corner2 % 6) or ((corner1) % 6) == ((corner2 + 1) % 6):
			print "neighboring corners"
			return point1, point2, level2
		if ((corner1 + 2) % 6) == (corner2 % 6) or ((corner1) % 6) == ((corner2 + 2) % 6):
			print "corners off by 2 angles"
			return point1, point2, level2 + level1
		if ((corner1 + 3) % 6) == (corner2 % 6):
			# or ((corner1) % 6) == ((corner2 + 2) % 6):
			print "corners off by 3 angles"
			return point1, point2, level2 + level1

def distance_one_corner(point1, point2):
		print "both corners"
		level1, quadrant1, corner1, level_offset1 = level_quadrant_corner(point1)
		level2, quadrant2, corner2, level_offset2 = level_quadrant_corner(point2)

#one corner and neighboring quadrant
		if (corner1 % 6 == quadrant2 % 6) or (corner1 % 6 == (quadrant2 + 1) % 6) or (corner2 % 6 == quadrant1 % 6) or (corner2 % 6 == (quadrant1 + 1) % 6):
			print "one corner and one neighboring quadrant"
			if corner1 < 0:
				#swap everything so corner1 is the point on a croner
				temp_point = point1
				temp_corner = corner1
				temp_level = level1
				temp_quadrant = quadrant1
				temp_offset = level_offset1
				point1 = point2
				corner1 = corner2
				level1 = level2
				quadrant1 = quadrant2
				level_offset1 = level_offset2
				point2 = temp_point
				corner2 = temp_corner
				level2 = temp_level
				quadrant2 = temp_quadrant
				level_offset2 = temp_offset

			if quadrant2 < corner1 or (corner1 == 2 and quadrant2 == 7): 
				level_offset2 = level2 - level_offset2
				
				print "point1 = " + str(point1) + " level1 = " + str(level1) + " corner1 = " + str(corner1) + " quadrant1 = " + str(quadrant1) + " level1_offset1 = " + str(level_offset1)
				print "point2 = " + str(point2) + " level2 = " + str(level2) + " corner2 = " + str(corner2) + " quadrant2 = " + str(quadrant2) + " level1_offset2 = " + str(level_offset2)
					
			if level1 == level2:
				print "same level"
				return point1, point2, level_offset2
			if level1 < level2:
				print "level 1 < level 2"
				if level1 >= level2-level_offset2:
					return point1, point2, level_offset2
				else:
					return point1, point2, level_offset2 + (level2 - level_offset2 - level1)
			if level1 > level2:
				print "level 1 > level 2"
				return point1, point2, level_offset2 + level1 - level2

	
def same_quadrant(point1, point2):
	level1, quadrant1, corner1, level_offset1 = level_quadrant_corner(point1)
	level2, quadrant2, corner2, level_offset2 = level_quadrant_corner(point2)
	print "same quadrant, not corners"
	if level1 == level2:
		print "same level"
		return point1, point2, abs(level_offset1 - level_offset2)
	if level1 < level2:
		print "level1 < level2"
		if level_offset2 == level_offset1:
			print "same level offset"
			return point1, point2, level2 - level1
		if abs(level_offset2 - level_offset1) > (level2 - level1):
			print "level difference less than offset difference"
			print point1, point2,  abs(level_offset2 - level_offset1) + level2 - level1
			return point1, point2,  abs(level_offset2 - level_offset1) + level2 - level1
		else:
			print "offset difference > level difference"
			print point1, point2, level2 - level1
			return point1, point2, level2 - level1
	return -1, -1, -1	
def get_distance(point1, point2):
		if point1 > point2:
			temp = point1
			point1 = point2
			point2 = temp
		
		if point1 == point2:
			print_result(point1, point2, 0)
		level1, quadrant1, corner1, level_offset1 = level_quadrant_corner(point1)
		level2, quadrant2, corner2, level_offset2 = level_quadrant_corner(point2)
		print "point1 = " + str(point1) + " level1 = " + str(level1) + " corner1 = " + str(corner1) + " quadrant1 = " + str(quadrant1) + " level1_offset1 = " + str(level_offset1)
		print "point2 = " + str(point2) + " level2 = " + str(level2) + " corner2 = " + str(corner2) + " quadrant2 = " + str(quadrant2) + " level1_offset2 = " + str(level_offset2)
		
		
#both are corners	
		if corner1>=0 and corner2>0:
			return distance_both_corners(point1, point2)
		#not corners, same quadrant
#one corner
		if (corner1 >= 0 and corner2 == -1) or (corner1 == -1 and corner2 >= 0):
			print "one corner and one quadrant"
			return distance_one_corner(point1, point2)

#both same quadrants
		if corner1 < 0 and corner2 < 0:
			if quadrant1 == quadrant2:
				return same_quadrant(point1, point2)
				
		print "did not find a path"
		return -1, -1, -1
	
if __name__ == "__main__":
#	print sys.argv
	if len(sys.argv) < 3 or len(sys.argv) > 4:
		usage()
	else:
		point1 = sys.argv[1]
		point2 = sys.argv[2]
		check_args(point1, point2)
		print "valid arguments"
		point1 = int(point1)
		point2 = int(point2)
		p1, p2, distance = get_distance(point1, point2)
#set it so point1 is always the lower number		
