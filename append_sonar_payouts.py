import Counter
import time_utils


#iterate through reports and add payout column


report_input = "E:\\play\\localdata_S138F004 S138J003_001\\sonar_processing\\sonar_data.csv"
report_fp = open(report_input,'r')
directory = "D:\\Dropbox (Centosette)_Hydromax\\PJ\\PuppytheaterUpload\\1539-Chattanooga,TN\\Source\\S138F004 S138J003_001"

counter = Counter.Counter(directory)

new_report = open("E:\\play\\localdata_S138F004 S138J003_001\\sonar_processing\\report_with_payouts.csv", 'w')
new_report.write(report_fp.readline())

for line in report_fp:
	line = line.rstrip()
	parts = line.split(",")
	filename = parts[0]
	new_payout = counter.get_closest_payout(time_utils.sonar_filename_to_ms(filename))
	new_report.write("{},{}\n".format(line,new_payout))

new_report.close()