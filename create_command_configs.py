import sys
import os
import glob
import Header
import Counter
import HD_index
import append_sonar_payouts
import sonar_graphs
import make_video_csv
#program to determine start and stop times and payouts given header file information.
#input header files
#input counter.ipd
#input figure out when start of time is?

meta_fp =  open("metadata.csv",'w')
meta_fp.write("Folder,USMH,DSMH,start time,stop time,start payout,stop payout,total payout,expected payout\n")




#	def get_time(self,percent):


#directory = sys.argv[1]
d = "D:/Dropbox (Centosette)_HMAX/PJ/PuppytheaterUpload/1628-Evansville,IN/Source"
directories = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o)) and not "4641" in o]
print directories
for directory in directories:
    folder = directory.split(os.sep)[-1]
    print "directory = {}".format(directory)
    print "folder = {}".format(folder)
    run_directory = "{}/localdata_{}".format(run_prefix,folder)
#    counter = Counter.Counter(directory)
    hd_index = HD_index.HD_index(directory)
    print "lines in counter file = {}".format(counter.length)

    print "USMH,DSMH,start time,stop time,start payout,stop payout"
    header_files = glob.glob("{}/Header_File_*.txt".format(directory))
    for header_file in header_files:
        curr_header = Header.Header(header_file)
        #copy folder
        #create command config
        #create bat file
        



#        sonar_graphs.sonar_graph(sonar_report_with_payouts,curr_header.radius,
#                counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStart)), 
#                counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStop)),
#                curr_header.USMH,
#                curr_header.DSMH,
#                run_directory
#                )
#        print "{},{},{},{},{},{},{},{},{}".format(
#            folder,
#            curr_header.USMH,
#            curr_header.DSMH, 
#            hd_index.convert_scroll_to_time(curr_header.scrollStart),
#            hd_index.convert_scroll_to_time(curr_header.scrollStop),
#            counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStart)),
#            counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStop)), 
#            counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStop)) - counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStart)),
#            curr_header.endDistance
#            )
#        meta_fp.write("{},{},{},{},{},{},{},{},{}\n".format(
#            folder,
#            curr_header.USMH,
#            curr_header.DSMH, 
#            hd_index.convert_scroll_to_time(curr_header.scrollStart),
#            hd_index.convert_scroll_to_time(curr_header.scrollStop),
#            counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStart)),
#            counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStop)), 
#            counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStop)) - counter.get_closest_payout(hd_index.convert_scroll_to_time(curr_header.scrollStart)),
#            curr_header.endDistance
#            ))
#        make_video_csv.create_csv(directory, run_directory, header_file) 

#print "closest to {} is {}".format(606688,counter.get_closest_payout(606688))



#def create_csv(raw_directory, run_directory, header_file):
#    localdata_short = os.path.split(run_directory)
#
#    hd_index = HD_index.HD_index(source_directory)
#    sonar_counter = Counter.Counter(source_directory)
#    sonar_data = Sonar_data.Sonar_data(run_directory)
#    curr_header = Header.Header(header_file)

