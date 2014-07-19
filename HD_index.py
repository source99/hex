import glob
from time_utils import convert_hex_line_to_ms

class HD_index:
#2014_06_06_13_38_35421    
    def __init__(self, directory):
        self.times = []
        index_file = glob.glob("{}\\HiRes\\*\\*\\lightson.ist".format(directory))[0]
        fp = open(index_file,'rb')
        line = fp.read(22)
        while len(line) == 22:
            self.times.append(convert_hex_line_to_ms(line))
            fp.read(1)
            line = fp.read(22)


    def convert_scroll_to_time(self, scroll):
        index = int(len(self.times)*scroll)
        return self.times[index]

