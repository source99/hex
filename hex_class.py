import sys

class full_point:
	def __init__(self, point):
		self.point = point
#determine level		
		level_int = float(1)
		if point == 1:
			level_int = 0
		elif point <=7:
				level_int = 1
		else:
			while point >= (((level_int / 2) + 0.5) * level_int) * 6 + 2:
				level_int +=1	
		self.level = level_int
		corner_2 = ((((level_int-1) / 2) + 0.5) * (level_int-1)) * 6 + 2 + level_int-1
		corner_3 = corner_2 + level_int
		corner_4 = corner_3 + level_int
		corner_5 = corner_4 + level_int
		corner_6 = corner_5 + level_int
		corner_7 = corner_6 + level_int
#		print corner_2, corner_3, corner_4, corner_5, corner_6, corner_7 
#determine corner
		corner_int = -1
		if level_int == 0:
			corner_int = 0
		elif point <= 7:
			corner_int = point
			corner_val = point
		elif point == corner_2:
			corner_int = 2
			corner_val = corner_2
		elif point == corner_3:
			corner_int = 3
			corner_val = corner_3
		elif point == corner_4:
			corner_int = 4
			corner_val = corner_4
		elif point == corner_5:
			corner_int = 5
			corner_val = corner_5
		elif point == corner_6:
			corner_int = 6
			corner_val = corner_6
		elif point == corner_7:
			corner_int = 7		
			corner_val = corner_7
		self.corner = corner_int
		if corner_int == -1:
			self.is_corner = False
		else:
			self.is_corner = True
#determine quadrant
#quadrant is determined by moving counterclockwise until landing on a corner		
		quadrant_int = -1
		if point <= 7:
			quadrant_int = -1
		elif corner_int > -1:
			quadrant_int = -1
		elif point < corner_2: 
			quadrant_int =  7
		elif point < corner_3: 
			quadrant_int =  2
		elif point < corner_4: 
			quadrant_int =  3
		elif point < corner_5: 
			quadrant_int =  4
		elif point < corner_6: 
			quadrant_int =  5
		elif point < corner_7: 
			quadrant_int =  6
		self.quadrant = quadrant_int
		if quadrant_int == -1:
			self.is_quadrant = False
		else:
			self.is_quadrant = True
#determine left and right offsets
#rightoffset is how many spaces to the right need to move from corner to get to point
#leftoffset is how many spaces to the left need to move from corner to get to point
		left_offset_int = 0
		right_offset_int = 0
		if corner_int > 0:
			left_offset_int = 0
			right_offset_int = 0
		elif quadrant_int == 7:
			right_offset_int = corner_2 - point
			left_offset_int = level_int - right_offset_int
		elif quadrant_int == 2:
			right_offset_int = corner_3 - point
			left_offset_int = point - corner_2
		elif quadrant_int == 3:
			right_offset_int = corner_4 - point
			left_offset_int = point - corner_3
		elif quadrant_int == 4:
			right_offset_int = corner_5 - point
			left_offset_int = point - corner_4
		elif quadrant_int == 5:
			right_offset_int = corner_6 - point
			left_offset_int = point - corner_5
		elif quadrant_int == 6:
			right_offset_int = corner_7 - point
			left_offset_int = point - corner_6
		self.right_offset = right_offset_int
		self.left_offset = left_offset_int





