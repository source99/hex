import hex_functions
import sys



def usage():
	print "Usage:>b_heif.py positive_integer positive_integer"
	print "program will return distance between those points"
	print "or"
	print "Usage:>b_heif.py filename"
	print "filename must be a csv file with the following format"
	print "point, point, correct distance between them"
	print "point must be a positive integer"
    

if __name__ == "__main__":
  if len(sys.argv) == 2:
  	check_file
  	call with file
  if len(sys.argv) == 3:
    check args are positive integers not 0
  else:
  	if len
    process_args
