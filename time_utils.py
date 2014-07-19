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

def sonar_filename_to_ms(filename):
#2014_06_06_10_54_37125
	filename = filename.rstrip(".png")
	parts = filename.split("_")
	return int(parts[3])*60*60*1000 + int(parts[4])*60*1000 + int(parts[5])

def convert_hex_line_to_ms(line):
#2014_06_06_13_38_35421	
    long_form = line.rstrip()#.decode("hex")
    parts = long_form.split("_")
    return int(parts[3])*60*60*1000 + int(parts[4])*60*1000 + int(parts[5])