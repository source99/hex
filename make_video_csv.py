import HD_index
import Counter
import Header
import Sonar_data
import os

#source_directory = "/Users/matt/work/centosette/hmax/Dropbox/PJ/PuppytheaterUpload/1539-Chattanooga,TN/Source/S138F004 S138J003_001"
#run_directory = "/Users/matt/work/centosette/hmax/runs/localdata_S138F004_S138J003_001"
#header_file = source_directory + "/Header_File_001.txt"
#localdata_short = "localdata_S138F004_S138J003_001"

#HD frame, sonar frame, payout, water height, sediment height, sediment sq inches, date, time

def create_csv(raw_directory, run_directory, header_file):
    localdata_short = os.path.split(run_directory)[1]

    hd_index = HD_index.HD_index(raw_directory)
    sonar_counter = Counter.Counter(raw_directory)
    sonar_data = Sonar_data.Sonar_data(run_directory)
    curr_header = Header.Header(header_file)



    start_time = hd_index.convert_scroll_to_time(curr_header.scrollStart)
    stop_time = hd_index.convert_scroll_to_time(curr_header.scrollStop) 

    hd_list_times = hd_index.get_range(start_time, stop_time)

    start_payout = sonar_counter.get_closest_payout(start_time)
    stop_payout = sonar_counter.get_closest_payout(stop_time) 

    csv_video_filename = "{}/{}_{}_video_inputs.csv".format(run_directory, curr_header.USMH, curr_header.DSMH)
    csv_video = open(csv_video_filename,'w')

    #get date
    csv_video.write("hd_image_name, sonar_image_name, frame_time, clock_time_hour, clock_time_min, clock_time_ms, payout, water_height_inches, sediment_height_inches, capacity_missing_percentage\n")

    for frame_time in hd_list_times:
        #get HD image name
        hd_image_name = localdata_short + "/hires/jpg/" + hd_index.get_frame_name(frame_time)
        sonar_index = sonar_data.get_frame_index_ms(frame_time)
        sonar_image_name = localdata_short + "/masked/" + sonar_data.image_file_name[sonar_index]
        clock_time_hour = hd_image_name[-15:-13]
        clock_time_min = hd_image_name[-12:-10]
        clock_time_ms = hd_image_name[-9:-4]
        payout = sonar_counter.get_closest_payout(frame_time) 
        water_height_inches = sonar_data.water_height_inches[sonar_index] 
        sediment_height_inches = sonar_data.max_sed_height_inches[sonar_index]
        capacity_missing_percentage = sonar_data.capacity_missing_percentage[sonar_index]
        print "{},{},{},{},{},{},{},{},{},{}".format(hd_image_name, sonar_image_name, frame_time, clock_time_hour, clock_time_min, clock_time_ms, payout, water_height_inches, sediment_height_inches, capacity_missing_percentage)
        csv_video.write("{},{},{},{},{},{},{},{},{},{}\n".format(hd_image_name, sonar_image_name, frame_time, clock_time_hour, clock_time_min, clock_time_ms, payout, water_height_inches, sediment_height_inches, capacity_missing_percentage))

    csv_video.close()
