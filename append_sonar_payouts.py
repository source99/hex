import Counter
import time_utils


#iterate through reports and add payout column


#report_input = "/Users/matt/work/centosette/HMAX_Runs/localdata_S138F004_S138J003_001/sonar_processing/report_data.csv"

#new_report = open("/Users/matt/work/centosette/HMAX_Runs/localdata_S138F004_S138J003_001/sonar_processing/report_with_payouts.csv", 'w')
#directory = "/Users/matt/work/centosette/hmax_dropbox/Dropbox (Centosette)/PJ/PuppytheaterUpload/1539-Chattanooga,TN/Source/S138F004 S138J003_001/" 


def append_payout(orig_report, new_report, directory): 
    counter = Counter.Counter(directory)
    new_report_fp = open(new_report,'w')
    report_fp = open(orig_report,'r')
    line = report_fp.readline().rstrip()
    line = line + ",payout\n"
    new_report_fp.write(line)

    for line in report_fp:
        line = line.rstrip()
        parts = line.split(",")
        filename = parts[0]
        new_payout = counter.get_closest_payout(time_utils.sonar_filename_to_ms(filename))
        new_report_fp.write("{},{}\n".format(line,new_payout))

    new_report_fp.close()
    return
