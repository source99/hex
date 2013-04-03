import hex_functions
import hex_tester
import sys
import time


point1 = int(sys.argv[1])
point2 = int(sys.argv[2])
start_time = time.clock()
distance = hex_functions.get_distance_ints(point1, point2)
elapsed_time = time.clock() - start_time

print "elapsed_time = " + str(elapsed_time)
