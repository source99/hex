import sys
import offsets_functions as offsets
import get_baseline_sonar as baseline
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import cv2.cv as cv
import cv2



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
 #   print "max height of pixels = " + str(max_height)
#   print "inches per pixel = " + str(float(float(96) / float(max_height)))
    return float(float(diameter) / float(max_height))

def parse_sonar_log(log_file, payout_start, payout_stop, pipe_radius_inches):
#image_file_name,max_sed_height_pixels, max_sed_height_inches,water_height, capacity_missing_pixels, capacity_missing_percentage, x_error, y_error, payout
#2014_06_06_10_54_38921.png,2,0.782608695652,39.7510080556,33,0.126664875446, 89, 130, payout
#   sonar_log_file_string = "image_file_name" + "," + "water_height" + "," + "valid_data" + "," + "payout, max_sediment_height, capacity_percent, x_error, y_error\n"
    fp = open(log_file,'r')
    fp.readline()
    payout = []
    water_height = []
    sed_height = []
    capacity_missing_percentage = []

    zoom_amount = -17
    orig_template = cv.LoadImageM("template_curve_full.png", cv.CV_LOAD_IMAGE_GRAYSCALE)
    zoom_template = offsets.zoom_wrapper(orig_template, zoom_amount)
    new_pixel_height_inches = baseline.calc_height_pixels(zoom_template, pipe_radius_inches*2)
    pixel_height_inches = 0.391304347826
    print "original {} : new {}".format(0.391304347826,new_pixel_height_inches)


    for line in fp:
        parts = line.split(",")
        payout_check = int(parts[-1])
        if payout_check > payout_start and payout_check < payout_stop:
            sed_height.append(float(parts[2]))
            water_height_input = float(parts[3])
            orig_y_offset_value = 115 - (water_height_input-3)/pixel_height_inches
            new_water_height = pipe_radius_inches - orig_y_offset_value*new_pixel_height_inches  
            print "{} : {} : {} : {}".format(parts[0],water_height_input, orig_y_offset_value, new_water_height)

#            water_height.append(float(parts[3]))

            payout.append((int(parts[-1]) - payout_start) / 100)
            capacity_missing_percentage.append(float(parts[5]))
            water_height.append(new_water_height)


    return sed_height, water_height, capacity_missing_percentage, payout




#log_file = "/Users/matt/work/centosette/hmax/runs/localdata_S138F004_S138J003_001/sonar_processing/report_with_payouts.csv"
#PIPE_RADIUS_INCHES = 18
#payout_start = 70
#payout_stop = 48580
#USMH = "USMH"
#DSMH = "DSMH"
#section_name = USMH + "_"+ DSMH

def sonar_graph(log_file, pipe_radius_inches, payout_start, payout_stop, USMH, DSMH, run_folder):
    secion_name =  USMH + "_"+ DSMH
    sed_height, water_height, capacity_missing_percentage, payout = parse_sonar_log(log_file,payout_start, payout_stop, pipe_radius_inches)
    plt.ylim([0,pipe_radius_inches*2 + 5])
    plt.stackplot(payout, water_height, color = (0,0,1))
    plt.stackplot(payout, sed_height, color = (.4,0,.15), linewidth=3)
    #plt.scatter(max_payout_s, 0, color = (0,0,0), s=0.5)
    plt.gcf().set_size_inches(6,2.2)
    plt.axhline(y=pipe_radius_inches*2, color = (0,0,0))
    plt.grid(True)
    #plt.xlim([0,xmax])

    graph_output_filename = "{}/graphs/sonar_sediment_600x220px_".format(run_folder) + section_name + ".png"
    os.mkdir("{}/graphs/{}".format(run_folder, section_name)
    plt.savefig(graph_output_filename,dpi=100)
    max_payout = max(payout)


    sections500 = max_payout / 500 + 1

    for section in range(0, sections500):
        x_start = (section) * 500
        x_stop = (section + 1)* 500


#sonar and sediment only
        plt.figure()
        plt.ylim([0,pipe_radius_inches*2 + 5])
        plt.stackplot(payout, water_height, color = (0,0,1))
        plt.stackplot(payout, sonar_x, color = (.4,0,.15), linewidth=3)
        plt.gcf().set_size_inches(6,2.2)
        plt.axhline(y=PIPE_RADIUS_INCHES*2, color = (0,0,0))
        plt.grid(True)
        plt.xlim(x_start,x_stop)
        graph_output_filename = "graphs/" + section_name + "/graph_sonar_combo(" + str(x_start) + "-" + str(x_stop) + ").png"			
        plt.savefig(graph_output_filename,dpi=600, transparent=True)

        
    return 
