import sys
import glob
import Header
import Counter
import HD_index
#program to determine start and stop times and payouts given header file information.
#input header files
#input counter.ipd
#input figure out when start of time is?

meta_fp =  open("metadata.csv",'w')
meta_fp.write("Folder,USMH,DSMH,start time,stop time,start payout,stop payout,total payout,expected payout\n")




#	def get_time(self,percent):


#directory = sys.argv[1]
directory = "D:\\Dropbox (Centosette)_Hydromax\\PJ\\PuppytheaterUpload\\1539-Chattanooga,TN\\Source\\S138F004 S138J003_001"
top_directory =  "D:\\Dropbox (Centosette)_Hydromax\\PJ\\PuppytheaterUpload\\1539-Chattanooga,TN\\Source\\"
directories = glob.glob("{}\\*".format(top_directory))
run_prefix = "E:/hmax/runs"
print directories
for directory in directories[2:]:
	folder = directory.split("\\")[-1]
    run_directory = "{}/{}".format(run_prefix,folder)

	counter = Counter.Counter(directory)
	hd_index = HD_index.HD_index(directory)
	print "lines in counter file = {}".format(counter.length)

	print "USMH,DSMH,start time,stop time,start payout,stop payout"
	header_files = glob.glob("{}\\Header_File_*.txt".format(directory))
	for header_file in header_files:
		curr_header = Header.Header(header_file)
		print "{},{},{},{},{},{},{},{},{}".format(
			folder,
			curr_header.USMH,
			curr_header.DSMH, 
			hd_index.convert_scroll_to_time(curr_header.scrollStart),
			hd_index.convert_scroll_to_time(curr_header.scrollStop),
			counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStart)),
			counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStop)), 
			counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStop)) - counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStart)),
			curr_header.endDistance
			)
		meta_fp.write("{},{},{},{},{},{},{},{},{}\n".format(
			folder,
			curr_header.USMH,
			curr_header.DSMH, 
			hd_index.convert_scroll_to_time(curr_header.scrollStart),
			hd_index.convert_scroll_to_time(curr_header.scrollStop),
			counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStart)),
			counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStop)), 
			counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStop)) - counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStart)),
			curr_header.endDistance
			))
        create_csv(directory, run_directory, header_file) 

#print "closest to {} is {}".format(606688,counter.get_closest_payout(606688))



#def create_csv(raw_directory, run_directory, header_file):
#    localdata_short = os.path.split(run_directory)
#
#    hd_index = HD_index.HD_index(source_directory)
#    sonar_counter = Counter.Counter(source_directory)
#    sonar_data = Sonar_data.Sonar_data(run_directory)
#    curr_header = Header.Header(header_file)

