import sys
import glob

#program to determine start and stop times and payouts given header file information.
#input header files
#input counter.ipd
#input figure out when start of time is?

SCROLL_OFFSET = 0.01

class Header:
    
    def __init__(self, file_name):
        self.scrollStart = 0
        self.scrollStop = 0
        self.year = 0
        self.month = 0
        self.day = 0
        self.USMH = ""
        self.DSMH = ""
        fp = open(file_name,'r')
        for line in fp:
        	parts = line.split("=")
        	if "Scroll Start" in parts[0]:
        		self.scrollStart = float(parts[1])
        	if "Scroll End" in parts[0]:
        		self.scrollStop = float(parts[1])
        	if "Year" in parts[0]:
        		self.year = int(parts[1])
        	if "Month" in parts[0]:
        		self.month = int(parts[1])
        	if "Day" in parts[0]:
        		self.day = int(parts[1])
        	if "Downstream MH" in parts[0]:
        		self.DSMH = parts[1].rstrip()
        	if "Upstream MH" in parts[0]:
        		self.USMH = parts[1].rstrip()

def convert_directory_to_ms(time_string):
#HH_MM_SS_MSSSS
	hours = int(time_string.split("_")[0])
	minutes = int(time_string.split("_")[1])
	seconds = int(time_string.split("_")[2])
	mseconds = int(time_string.split("_")[3])
	return hours*60*60*1000 + minutes*60*1000 + seconds*1000 + mseconds

def convert_ms_to_time(start_ms):
	hours = "{}".format(start_ms / (60*60*1000)).zfill(2)
	remaining_ms = start_ms % (60*60*1000)
	minutes = "{}".format(remaining_ms / (60*1000)).zfill(2)
	ms = "{}".format(remaining_ms % (60*1000)).zfill(5)
	return "{}_{}_{}".format(hours, minutes, ms)


class Counter:

	def __init__(self, file_name, start_time):
		fp = open(file_name,'r')
		self.file_contents = fp.readlines()
		self.length = len(self.file_contents)
		self.start_time = start_time
		self.start_time_ms = convert_directory_to_ms(start_time)

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

#	def get_time(self,percent):


#directory = sys.argv[1]
directory = "D:\\Dropbox (Centosette)_Hydromax\\PJ\\PuppytheaterUpload\\1539-Chattanooga,TN\\Source\\S138F004 S138J003_001"
print directory
folder = directory.split("\\")[-1]
#counter
counter = glob.glob("{}\\Counter\\*\\*\\Counter.ipd".format(directory))
start_time = counter[0].split("\\")[-2]
print "start time = {}".format(start_time)
#start_time = 

counter = Counter(counter[0], start_time)
print "lines in counter file = {}".format(counter.length)

print "USMH,DSMH,start time,stop time,start payout,stop payout"
header_files = glob.glob("{}\\Header_File_*.txt".format(directory))
for header_file in header_files:
	curr_header = Header(header_file)
	print "{},{},{},{},{},{},{},{},{},{}".format(
		folder,
		curr_header.USMH,
		curr_header.DSMH, 
		counter.get_ms((curr_header.scrollStart) / 100.0),
		counter.get_ms((curr_header.scrollStop) / 100.0),
		counter.get_time((curr_header.scrollStart) / 100.0),
		counter.get_time((curr_header.scrollStop) / 100.0),
		counter.get_payout((curr_header.scrollStart) / 100.0),
		counter.get_payout((curr_header.scrollStop) / 100.0), 
		counter.get_payout((curr_header.scrollStart) / 100.0) - counter.get_payout((curr_header.scrollStop+1) / 100.0)
		)
