import move_image
import sys
import os
import offsets_functions as offsets
import cv2.cv as cv
import cv2


'''
circle_file = sys.argv[1]

circle = cv.LoadImageM(circle_file, cv.CV_LOAD_IMAGE_GRAYSCALE)
lines = cv.CreateMat(600,600, cv.CV_8UC1)

sum_heights = 0	

for x in range(0,600):
	height_up = 0
	height_down = 0
	found = False
	for y in range(0,600):
		if cv.Get2D(circle,y,x)[0] > 0:
			while cv.Get2D(circle,y+1,x)[0] > 0:
				y+=1
				sum_heights+=1
			found = True
			break
	if found:
		for ys in range(y+1,600):
			if cv.Get2D(circle,ys,x)[0] > 0:
				height_down = ys - y;
				cv.Line(lines, (x,y), (x,ys), 254, 1,8,0)
				break
		print "At X=" + str(x) + "found line from " +str(y) + " to " + str(ys) 
		sum_heights = sum_heights + height_down
print "total sum = " + str(sum_heights)
cv.ShowImage("area", lines)
cv.WaitKey()	
		
'''		
		
def circle_area(circle):
	
	lines = cv.CreateMat(600,600, cv.CV_8UC1)
	#circle = cv.LoadImageM(circle_file, cv.CV_LOAD_IMAGE_GRAYSCALE)

	sum_heights = 0	

	for x in range(0,600):
		height_up = 0
		height_down = 0
		found = False
		for y in range(0,600):
			if cv.Get2D(circle,y,x)[0] > 0:
				while cv.Get2D(circle,y+1,x)[0] > 0:
					y+=1
					sum_heights+=1
				found = True
				break
		if found:
			for ys in range(y+1,600):
				if cv.Get2D(circle,ys,x)[0] > 0:
					height_down = ys - y;
					cv.Line(lines, (x,y), (x,ys), 254, 1,8,0)
					break
			#print "At X=" + str(x) + "found line from " +str(y) + " to " + str(ys) 
			sum_heights = sum_heights + height_down
#	print "total sum = " + str(sum_heights)
	#cv.ShowImage("area", lines)
	#cv.WaitKey()	

	return sum_heights
	
	
def calc_height_pixels(circle, diameter):
	max_height = 0
	x_of_max = 0
	for x in range(0,600):
		curr_y = 0
		extra_height = 0
		for y in range(599, 0, -1):
			if cv.Get2D(circle,y,x)[0] > 0:
				while cv.Get2D(circle,y-1,x)[0] > 0:
					y-=1
					curr_y = y
					extra_height = extra_height + 1
				break
		for ys in range(curr_y, 0, -1):
			if cv.Get2D(circle,ys,x)[0] > 100:
				found_height = y - ys + extra_height
				if found_height > max_height:
					max_height = found_height
					x_of_max = x
					#print "calculating height of pixels - found max height at " + str(x) + " height = " + str(max_height)
#	print "max height of pixels = " + str(max_height)
#	print "inches per pixel = " + str(float(float(96) / float(max_height)))
	return float(float(diameter) / float(max_height))
