import cv2.cv as cv
import cv2
import numpy as np
import math
import sys
import glob
import os
REQUIRED_CIRCLESNESS = 0.95
def process_frame(filename):
    im = cv2.imread(filename)
    filename = filename.replace("rectified","enhanced_ellipse_overlay") 
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    is_black_y,is_black_x = np.where(thresh == np.array([0]))
    is_black = np.column_stack((is_black_x,is_black_y))
    ellipse = cv2.fitEllipse(is_black)
    cv2.ellipse(im,ellipse,(0,255,255),2)
    #print ellipse
    center = (int(ellipse[0][0]),int(ellipse[0][1]))
    Height = ellipse[1][0]
    Width = ellipse[1][1]
    circleness_percent = Height / float(Width)
    if circleness_percent > REQUIRED_CIRCLESNESS:
        found_circle = True
    else:
        found_circle = False
    angle_offset = ellipse[2]

    x_delta = is_black_x - center[0]
    y_delta = center[1] - is_black_y

    x_square = np.square(x_delta)
    y_square = np.square(y_delta)

    sum_square = x_square + y_square

    is_black_radii = np.sqrt(sum_square)
    radians = np.arctan2(y_delta, x_delta)
    angles = np.degrees(radians)
    angles = [-1 * angle + 180 if angle < 0 else angle for angle in angles]

    fp = open("laser/points/{}_points.csv".format(os.path.split(filename)[1].replace(".png","")), 'w')
    fp_angles = open("laser/angles/{}_angles.csv".format(os.path.split(filename)[1].replace(".png","")), 'w')
    fp.write("center_x,center_y,point_x,point_y,radius,angle,angle_radians\n")
    fp_angles.write("angle,radius\n")
    average_radius = np.array(np.zeros(360))
    average_radius_points = np.array(np.zeros(360))
    index_max = np.argmax(is_black_radii)
    index_min = np.argmin(is_black_radii)
    cv2.line(im,center,(is_black_x[index_max],is_black_y[index_max]),(255,255,0),3)
    cv2.line(im,center,(is_black_x[index_min],is_black_y[index_min]),(255,0,255),3)
    cv2.imwrite(filename,im)

    if found_circle:
        print "{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(os.path.split(filename)[1],center[0],center[1],Height,Width,len(is_black),1,1,is_black_radii[index_max],is_black_x[index_max],is_black_y[index_max],is_black_radii[index_min],is_black_x[index_min],is_black_y[index_min])

        for i in range(0,len(is_black)):
            fp.write("{},{},{},{},{},{},{}\n".format(center[0],center[1],is_black_x[i],is_black_y[i],is_black_radii[i],angles[i],radians[i]))
            angle_index = angles[i] / 1
            average_radius[angle_index] = average_radius[angle_index] + is_black_radii[i]
            average_radius_points[angle_index] = average_radius_points[angle_index] + 1
        fp.close()

        for i in range(0,len(average_radius_points)):
            if average_radius_points[i] > 0:
                average_radius[i] = average_radius[i] / float(average_radius_points[i])
            fp_angles.write("{},{}\n".format(i,average_radius[i]))
    else:
        print "{},-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1".format(os.path.split(filename)[1])

    fp_angles.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: fit_ellipse.py start_index, stop_index"
        exit(-1)
    else:
        start_index = int(sys.argv[1])
        stop_index = int(sys.argv[2])
        laser_frames = glob.glob("laser/camall/rectified/*.png")
        if start_index == 0:
            print "Filename, Ctr.x, Ctr.y, H, W, Pts, Thresh, OvalPct, MaxD, MaxD.x, MaxD.y, MinD, MinD.x, MinD.y"
        for i in range(0,len(laser_frames)):
            if i >= start_index and i < stop_index:
                frame = laser_frames[i]
                process_frame(frame)

