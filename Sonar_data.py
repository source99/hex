import glob
import bisect
from time_utils import convert_hex_line_to_ms, convert_ms_to_time, convert_filename_line_to_ms

class Sonar_data:
#image_file_name,max_sed_height_pixels, max_sed_height_inches,water_height, capacity_missing_pixels, capacity_missing_percentage, x_error, y_error
#2014_06_06_10_54_38921.png,2,0.782608695652,39.7510080556,33,0.126664875446, 89, 130,0

    def __init__(self, directory):
        report_file = "{}/sonar_processing/report_with_payouts.csv".format(directory)
        fp = open(report_file,'r')
        line = fp.readline()
        line = fp.readline()
        filename = line.split(",")[0]
        self.date = filename[0:9]
        fp.close()
        fp = open(report_file,'r')
        fp.readline()
        self.times = []
        self.image_file_name = []
        self.max_sed_height_pixels = []
        self.max_sed_height_inches = []
        self.water_height_inches = []
        self.capacity_missing_pixels = []
        self.capacity_missing_percentage = []
        self.payout = []
        for line in fp:
            line.rstrip()
            parts = line.split(",")
            self.image_file_name.append(parts[0])
            self.max_sed_height_pixels.append(int(parts[1]))
            self.max_sed_height_inches.append(float(parts[2]))
            self.water_height_inches.append(float(parts[3]))
            self.capacity_missing_pixels.append(int(parts[4]))
            self.capacity_missing_percentage.append(float(parts[5]))
            self.payout.append(int(parts[-1]))
            self.times.append(convert_filename_line_to_ms(parts[0]))


    def get_frame_name_ms(self,ms):
        index = bisect.bisect_left(self.times,ms)
        return self.image_file_name[index]

    def get_frame_index_ms(self,ms):
        return bisect.bisect_left(self.times,ms)
