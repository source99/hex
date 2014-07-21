from time_utils import convert_directory_to_ms, convert_ms_to_time
import bisect
import collections
import glob
SCROLL_OFFSET = 0.00

class Counter:

    def __init__(self, directory):
        folder = directory.split("/")[-1]
        counter_file = glob.glob("{}/Counter/*/*/Counter.ipd".format(directory))[0]
        start_time_directory = counter_file.split("/")[-2]
        fp = open(counter_file,'r')

        self.ms_to_payout_mapping = collections.OrderedDict()
        self.payout_to_ms_mapping = {}
        self.file_contents = fp.readlines()
        self.length = len(self.file_contents)
        self.start_time_ms = convert_directory_to_ms(start_time_directory)
        for line in self.file_contents:
            #payout;ms
            payout,ms = line.rstrip().split(";")
            payout = int(payout)
            ms = int(ms)
            self.ms_to_payout_mapping[ms+self.start_time_ms] = payout
#           self.ms_to_payout_mapping[ms] = payout
            self.payout_to_ms_mapping[payout] = [ms+self.start_time_ms]
        fp.close()

    def get_closest_payout(self,ms_input):
        index = bisect.bisect_left(self.ms_to_payout_mapping.keys(),ms_input)
        return self.ms_to_payout_mapping.values()[index]


    def get_payout(self, percent):
        index = int(self.length * (percent+SCROLL_OFFSET))
        line = self.file_contents[index]
        payout = int(line.split(";")[0])
        return payout / 100.0
    def get_ms(self,percent):
        index = int(self.length * (percent+SCROLL_OFFSET))
        line = self.file_contents[index]
        ms_time = int(line.split(";")[1])
        return ms_time
    def get_time(self,percent):
        index = int(self.length * (percent+SCROLL_OFFSET))
        line = self.file_contents[index]
        ms_time = int(line.split(";")[1]) + self.start_time_ms
        return convert_ms_to_time(ms_time)
        return ms_time


def create_counter_from_directory(directory):
    folder = directory.split("\\")[-1]
    counter = glob.glob("{}\\Counter\\*\\*\\Counter.ipd".format(directory))
    start_time = counter[0].split("\\")[-2]
    print "start time = {}".format(start_time)
    counter = Counter.Counter(counter[0], start_time)
    return counter
