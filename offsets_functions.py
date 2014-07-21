import cv2.cv as cv
import cv2
import numpy as np
max_x_pixels = 600
max_y_pixels = 600


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
		x_coord = int((src_image.rows - rows)/2)
		y_coord = int((src_image.cols - cols)/2)
    ###print x_coord,y_coord,rows,cols,blank_image.rows,blank_image.cols
		
		zoom_img =  cv.CreateMat(rows, cols, src_image.type)
		blank_image = cv.CreateMat(src_image.rows, src_image.cols, src_image.type)
		cv.Set(zoom_img,0)
		cv.Set(blank_image,0)
		cv.Resize(src_image, zoom_img)
#		print "from inside zoom function: " + str(x_coord) + " " + str(y_coord) + " " + str(rows) + " " + str(cols) + " " + str(blank_image.rows) + " " + str(blank_image.cols)
		temp_array = cv.GetSubRect(blank_image, (x_coord,y_coord ,rows,cols)	)
		cv.Copy(zoom_img,temp_array)
		return blank_image
		
def zoom_in(src_image, zoom_amount):
#zooms in an image
#does this by creating a new matrix that is larger and copying the source image into that matrix with resize
#then trims the larger border	
#		zoom_img =  cv.CreateMat(int(src_image.rows * (1 + zoom_amount)), int(src_image.cols * (1 + zoom_amount)), src_image.type)
		final_image = cv.CreateMat(src_image.rows, src_image.cols, src_image.type)
		zoom_img =  cv.CreateMat(int(src_image.rows + (2 * zoom_amount)), int(src_image.cols + (2 * zoom_amount)), src_image.type)
		cv.Resize(src_image, zoom_img)
		sized_zoomed = cv.GetSubRect(zoom_img, (zoom_amount, zoom_amount, src_image.rows, src_image.cols))
		cv.Copy(sized_zoomed, final_image)
		return final_image
		
		
		
def zoom_wrapper(src_image, zoom_amount):
	final_image = cv.CreateMat(src_image.rows, src_image.cols, src_image.type)
	if(zoom_amount > 0):
		final_image = zoom_in(src_image, zoom_amount)
	if(zoom_amount < 0):
		final_image = zoom_out(src_image, abs(zoom_amount))
	if zoom_amount == 0:
		final_image = src_image
	return final_image
				