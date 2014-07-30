import cv2.cv as cv
import cv2
import numpy as np
import math

REQUIRED_CIRCLESNESS = 0.95

filename = "sample_fitellipse.png"
im = cv2.imread(filename)




#im = cv2.imread("fit_ellipse_test_bad.png")
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,0)
is_black_y,is_black_x = np.where(thresh == np.array([0]))
is_black = np.column_stack((is_black_x,is_black_y))


ellipse = cv2.fitEllipse(is_black)
cv2.ellipse(im,ellipse,(0,255,255),2)
print ellipse
center = (int(ellipse[0][0]),int(ellipse[0][1]))
Height = ellipse[1][0]
Width = ellipse[1][1]
circleness_percent = Height / float(Width)
if circleness_percent > REQUIRED_CIRCLESNESS:
    found_circle = True
else:
    found_circle = False
angle_offset = ellipse[2]
print "center = {}".format(center)
print "Height = {}".format(Height)
print "Width = {}".format(Width)
print "angle_offset = {}".format(angle_offset)
print "found circle = {}".format(found_circle)
print "max D = {}".format(Width / 2.0)
print "min D = {}".format(Height / 2.0)
MinD_x = int(center[0] + math.cos(angle_offset / 180.0) * Height / 2.0)
MinD_y = int(center[1] - math.sin(angle_offset / 180.0) * Height / 2.0)
MaxD_x = int(center[0] + math.cos((angle_offset - 90) / 180.0) * Width / 2.0)
MaxD_y = int(center[1] - math.sin((angle_offset - 90) / 180.0) * Width / 2.0)
print "MaxD_x = {}".format(MaxD_x)
print "MaxD_y = {}".format(MaxD_y)
print "MinD_x = {}".format(MinD_x)
print "MinD_y = {}".format(MinD_y)


cv2.line(im,center,(MinD_x,MinD_y),(255,0,0),3)
cv2.line(im,center,(MaxD_x,MaxD_y),(255,0,0),3)
cv2.imshow("ellipse",im)

print is_black

x_delta = is_black_x - center[0]
y_delta = center[1] - is_black_y

x_square = np.square(x_delta)
y_square = np.square(y_delta)

sum_square = x_square + y_square

is_black_radii = np.sqrt(sum_square)
print is_black_radii
    

radians = np.arctan2(y_delta, x_delta)
angles = np.degrees(radians)

angles = [-1 * angle + 180 if angle < 0 else angle for angle in angles]

print angles

fp = open("{}_points.csv".format(filename), 'w')
fp.write("center_x,center_y,point_x,point_y,radius,angle\n")
for i in range(0,len(is_black)):
    fp.write("{},{},{},{},{},{},{}\n".format(center[0],center[1],is_black_x[i],is_black_y[i],is_black_radii[i],angles[i],radians[i]))

fp.close()



#cv.WaitKey()
#Filename, Ctr.x, Ctr.y, H, W, Pts, Thresh, OvalPct, MaxD, MaxD.x, MaxD.y, MinD, MinD.x, MinD.y
#2014_03_30_17_41_51484.png,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1
#2014_03_30_17_41_51562.png,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1
#2014_03_30_17_41_51640.png,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1
#2014_03_30_17_41_51718.png,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1
#2014_03_30_17_41_51796.png,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1
#2014_03_30_17_41_51953.png,799.151,615.987,399.048,361.146,4282,56,11,174.837,697,473,34.1321,833,618

#cv2.ellipse(im,ellipse,(0,255,255),2)
#cv2.imshow("asdf",im)
#cv.WaitKey()


