import glob
from time_utils import convert_hex_line_to_ms, convert_ms_to_time

class HD_index:
#2014_06_06_13_38_35421    
    def __init__(self, directory):
        self.times = []
        index_file = glob.glob("{}/HiRes/*/*/lightson.ist".format(directory))[0]
        fp = open(index_file,'rb')
        line = fp.read(22)
        parts = line.rstrip().split("_")
        self.date = parts[0] + "_" + parts[1] + "_" + parts[2]
        while len(line) == 22:
            self.times.append(convert_hex_line_to_ms(line))
            fp.read(1)
            line = fp.read(22)


    def convert_scroll_to_time(self, scroll):
        index = int(len(self.times)*scroll)
        return self.times[index]
    def get_range(self, start_time, stop_time):
        result = [time for time in self.times if time >=start_time and time <= stop_time]
        return result
    def get_frame_name(self,ms):
        time_string = convert_ms_to_time(ms)
        return_val = self.date + "_" + time_string + ".jpg"
        return return_val
