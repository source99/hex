import sys
import os
import glob
import Header
import Counter
import HD_index
import append_sonar_payouts
import sonar_graphs
import make_video_csv
import subprocess
#program to determine start and stop times and payouts given header file information.
#input header files
#input counter.ipd
#input figure out when start of time is?

meta_fp =  open("metadata.csv",'w')
meta_fp.write("Folder,USMH,DSMH,start time,stop time,start payout,stop payout,total payout,expected payout\n")

AWS = False


#payoutdef get_time(self,percent):

if AWS:
    scratch_drive = "E:"
    d = "E:/Dropbox (Centosette)/PJ/PuppytheaterUpload/1628-Evansville,IN/Source"
    localdata_master = "E:/Dropbox (Centosette)/PJ/PuppytheaterUpload/localdata_master"
    scratch_space = "E:/"
else:
    d = "/Users/matt/work/centosette/hmax/Dropbox/PJ/PuppytheaterUpload/1628-Evansville,IN" 
    localdata_master = "/Users/matt/work/centosette/hmax/Dropbox/PJ/PuppytheaterUpload/localdata_master"
    scratch_space = "/Users/matt/work/centosette/hmax/Dropbox/PJ/PuppytheaterUpload/run_evansville"
    scratch_drive = "E:"

sonar_blank_radius = 20
sonar_threshold - 36
directories = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
print directories
for directory in directories:
    folder = directory.split(os.sep)[-1]
    print "directory = {}".format(directory)
    print "folder = {}".format(folder)
    header_files = glob.glob("{}/Header_File_*.txt".format(directory))
    localdata_folder = os.path.join(scratch_space,"localdata_{}".format(folder))
    if AWS:
        command = "xcopy /E /Y /I \"{}\" \"{}\"".format(localdata_master, localdata_folder)
    else:
        command = "cp -r \"{}\" \"{}\"".format(localdata_master,localdata_folder)
    print command
    subprocess.call(command)
    print localdata_folder
    command_fp = open("{}".format(os.path.join(localdata_folder,"command_config.csv"),'w')) 
    command_fp.write("Folder,USMH,DSMH,START_LASER,STOP_LASER,PIPE_DIAMETER,BLANK_RADIUS,SONAR_THRESHOLD\n")
    header_files = glob.glob("{}/Header_File_*.txt".format(directory))
    for header_file in header_files:
       curr_header = Header.Header(header_file) 
       command_fp.write("{},{},{},{},{},{},{},{}\n".format(folder,curr_header.USMH,curr_header.DSMH,curr_header.laser_start_frame,curr_header.laser_stop_frame,curr_header.pipe_size,sonar_blank_radius,sonar_threshold)),
    command_fp.close()    
    execute_batch = open("{}".format(os.path.join(localdata_folder,"run_all.bat"),'w'))
    execute_batch.write("{}\n".format(scratch_drive))
    execute_batch.write("cd \"{}\"\n".format(localdata_folder))
    execute_batch.write("python C:\Users\Administrator\Documents\GitHub\sonar\command_center.py\n")
    execute_batch.write("python C:\Users\Administrator\Documents\GitHub\sonar\command_center_sonar.py\n")
    execute_batch.write("python C:\Users\Administrator\Documents\GitHub\sonar\command_center_part2.py\n")
    execute_batch.close()





