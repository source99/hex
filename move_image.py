#!/usr/bin/env python #


import sys
import ImageFile
import cv2.cv as cv
import cv2
import os
import random
import numpy as np

x_offset = 0
y_offset = 0
zoom_offset = 0
mark_bad = -1
rotation_offset = 0


def remap_image(src_image, x_delta, y_delta):
#translates image in X and Y
#data that moves off the end of the image is lost
#does a very simple remap based on the x_delta or y_delta
		dest_img = cv.CreateMat(src_image.rows, src_image.cols, src_image.type)
		map_x = cv.CreateMat(src_image.rows, src_image.cols, cv.CV_32FC1)
		map_y = cv.CreateMat(src_image.rows, src_image.cols, cv.CV_32FC1)
		for i in range(0, map_x.rows): 
			for j in range(0, map_x.cols):
				map_x[i,j] = j + x_delta
				map_y[i,j] = i + y_delta
		cv.Remap(src_image, dest_img, map_x, map_y)
	
		return dest_img
		
def rotateImage(src_image, angle):
		image_center = (300,300)
		dest_img = cv.CreateMat(src_image.rows, src_image.cols, src_image.type)
#		dest_img = np.zeros((600, 600), np.float32)
		rot_mat = cv2.getRotationMatrix2D(image_center,angle,1.0)
		nump_image = np.asarray(src_image)
		nump_dest_img = np.asarray(dest_img)
		nump_dest_img2 = np.asarray(dest_img)
#		cv2.warpAffine(nump_image, nump_image, rot_mat, 0, 0)
		nump_dest_img = cv2.warpAffine(nump_image, rot_mat, nump_image.shape,flags=cv2.INTER_LINEAR)
		result = cv.fromarray(nump_dest_img)
		return result		
		
def zoom_out(src_image, zoom_amount):
#zooms out an image
#does this by creating a new matrix that is smaller and copying the source image into the smaller canvas
#by calling resize

#		rows = int(src_image.rows * (1 - zoom_amount))
#		cols = int(src_image.cols * (1 - zoom_amount))
		rows = src_image.rows - 2 * zoom_amount
		cols = src_image.cols - 2 * zoom_amount
		zoom_img =  cv.CreateMat(rows, cols, src_image.type)
		blank_image = cv.CreateMat(src_image.rows, src_image.cols, src_image.type)
		cv.Resize(src_image, zoom_img)
		temp_array = cv.GetSubRect(blank_image, (int((src_image.rows - rows)/2),int((src_image.cols - cols)/2) ,rows,cols)	)
		cv.Copy(zoom_img,temp_array)
		return blank_image
		
def zoom_in(src_image, zoom_amount):
#zooms in an image
#does this by creating a new matrix that is larger and copying the source image into that matrix with resize
#then trims the larger border	
#		zoom_img =  cv.CreateMat(int(src_image.rows * (1 + zoom_amount)), int(src_image.cols * (1 + zoom_amount)), src_image.type)
		zoom_img =  cv.CreateMat(int(src_image.rows + (2 * zoom_amount)), int(src_image.cols + (2 * zoom_amount)), src_image.type)
		cv.Resize(src_image, zoom_img)
		sized_zoomed = cv.GetSubRect(zoom_img, (zoom_amount, zoom_amount, src_image.rows, src_image.cols))
		cv.Copy(sized_zoomed, src_image)
		return src_image
		
		
def get_offsets(image_file_name, template_file):
#this function is called for each image.  
#it takes as input the image file, a template and the output file to write the offsets
#it uses global var x_offset, y_offset and zoom_offset to keep track of the most recent translations.
#it applies these translations to the image before it shows it each time.  


#initialization
		global x_offset, y_offset, zoom_offset, mark_bad,  rotation_offset
		print "input file is " + image_file_name
		image_file = image_file_name
#		image_file = image_file_name
		template = template_file
		cv_img = cv.LoadImageM(image_file, cv.CV_LOAD_IMAGE_GRAYSCALE)
		template_img = cv.LoadImageM(template, cv.CV_LOAD_IMAGE_GRAYSCALE)
		first = 1
		move_size = 10
		zoom_amount = 1
		command = -1
		alpha = 0.2
		beta = 1 - alpha
				

		orig_template_sized = cv.CreateMat(cv_img.rows, cv_img.cols, cv_img.type)
		template_sized = cv.CreateMat(cv_img.rows, cv_img.cols, cv_img.type)
		cv.Resize(template_img, orig_template_sized)
		template_sized = orig_template_sized

		combined_img = cv.CreateMat(cv_img.rows, cv_img.cols, cv_img.type)

		if(zoom_offset > 0):
#			for x in range(0,zoom_offset):
			template_sized = zoom_in(orig_template_sized, zoom_offset)
		if(zoom_offset < 0):
#			for x in range(zoom_offset,0):
			template_sized = zoom_out(orig_template_sized, abs(zoom_offset) )

#		if(zoom_offset > 0):
#			for i in range(0, zoom_offset):
#				template_sized = zoom_in(template_sized, 1)
#		if(zoom_offset < 0):
#				for i in range(0, abs(zoom_offset)):
#					template_sized = zoom_out(template_sized, 1 )


#		cv.AddWeighted( template_sized, alpha, cv_img, beta, 0.0, combined_img);
		cv_img = remap_image(cv_img, x_offset, y_offset)
		cv_img = rotateImage(cv_img, rotation_offset)

		
		while True:
				print 'enter the letter for command: arrow key to move, "," to zoom in, "." to zoom out, ? for done.'
				#command = msvcrt.getch()
				cv.AddWeighted( template_sized, alpha, cv_img, beta, 0.0, combined_img);
				cv.ShowImage("shifted combined", combined_img)
#				cv.ShowImage("shifted combined", template_sized)
				command = cv.WaitKey()
				print "command = " + str(command)
				cv.DestroyWindow("shifted combined")

				if(command == 44):
						print "zoom in"						
						zoom_offset = zoom_offset + zoom_amount
						template_sized = zoom_out(orig_template_sized, abs(zoom_offset))
				if(command == 46):
						print "zoom out"
						zoom_offset = zoom_offset - zoom_amount
						template_sized = zoom_out(orig_template_sized, abs(zoom_offset))
				if(command == 2424832):
						print "move left"
						cv_img = remap_image(cv_img, move_size, 0)
						x_offset = x_offset + move_size
				if(command == 2555904):
						print "move right"
						cv_img = remap_image(cv_img, -1 * move_size, 0)
						x_offset = x_offset - move_size
				if(command == 2490368):
						print "move up"
						cv_img = remap_image(cv_img, 0, move_size)
						y_offset = y_offset + move_size
				if(command == 2621440):
						print "move Down"
						cv_img = remap_image(cv_img, 0, -1 * move_size)
						y_offset = y_offset - move_size

				if(command == 111):
						print "rotating"
						cv_img = rotateImage(cv_img, 1)
						rotation_offset = rotation_offset + 1

				if(command == 112):
						print "rotating"
						cv_img = rotateImage(cv_img, -1)
						rotation_offset = rotation_offset - 1

				if(command == 100):
						print "toggling mark bit"
						mark_bad = mark_bad * -1
						

				if(command == 106):
						print "move left small"
						cv_img = remap_image(cv_img, 1, 0)
						x_offset = x_offset + 1
				if(command == 108):
						print "move right small"
						cv_img = remap_image(cv_img, -1, 0)
						x_offset = x_offset - 1
				if(command == 105):
						print "move up small"
						cv_img = remap_image(cv_img, 0, 1)
						y_offset = y_offset + 1
				if(command == 107):
						print "move Down small"
						cv_img = remap_image(cv_img, 0, -1)
						y_offset = y_offset - 1




				if(command == 13):
						break
				if(command == 113):
						exit()
	
				
		print "final offsets"
		print "x_offset = " + str(x_offset)
		print "y_offset = " + str(y_offset)
		print "zoom_offset = " + str(zoom_offset)
		print "mark_bad is " + str(mark_bad)
		print "rotation offset = " + str(rotation_offset)
		output_string = image_file_name + ", " + str(mark_bad) + ", " + str(x_offset) + ", " + str(y_offset) + ", " + str(zoom_offset) + ", " + str(rotation_offset) + '\n'
		#output_file.write(output_string)
		return cv_img, x_offset, y_offset, zoom_offset, rotation_offset
				
def usage():
    name = sys.argv[0] or "move_image.py"
    print('Usage: move_image.py IMAGE_DIRECTORY TEMPLATE')
    print('\tIMAGE DIRECTORY is a path to a directory containing images to be processed')
    print('\tTEMPLATE is an image that contains template of the pipe')
    print('\tUse the arrow keys and "," and "." to move around and zoom the images to align them.')
    print('\tThis program will output a csv file with the x, y and zoom offsets')

def loop_file(image_dir, template_file):
		#list_f = open(list_file, 'r')
		#list_string = list_f.read()
		#list = list_string.split('\x00')
		
		list =  [file for file in os.listdir(image_dir) if file.lower().endswith(".png")]
		output_file_name = "offsets_" + str(random.randrange(1,100+1)) + ".csv"
		output_file = open(output_file_name, 'w')
		count_files = 0 
		for filename in list:
			print filename
			get_offsets(filename, template_file, output_file)
			#if count_files > 100:
				#break
			#count_files += 1
			
			
if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
    else:
        loop_file(sys.argv[1], sys.argv[2])
