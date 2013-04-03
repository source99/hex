import hex_functions
import hex_tester
import sys



def usage():
	print "Usage:\n\t#b_heif.py point point"
	print "point must be a positive integer"
	print "program will return distance between those points"
	print "or"
	print "Usage:\n\t#b_heif.py filename"
	print "filename must be a csv file with the following format"
	print "point, point, correct distance between them"
	print "point must be a positive integer"
	exit()
  
def test_file(filename):
	hex_tester.test_specifics(filename)

  
if __name__ == "__main__":
	if len(sys.argv) == 2:
		try:
			with open(sys.argv[1]):
				test_file(sys.argv[1])
		except IOError:
			print sys.argv[1] + " file does not exist\n"
			usage()
	
	if len(sys.argv) == 3:
		if sys.argv[1] == "0" and sys.argv[2] == "0":
			#exit when both points are 0
			exit
		

		point1 = sys.argv[1]
		point2 = sys.argv[2]
		
		if not point1.isdigit():
			print "point 1 is not a positive integer"
			usage()
		if not point2.isdigit():
			print "point 2 is not a positive integer"
			usage()
		
		point1 = int(point1)
		point2 = int(point2)
		
		#point1 = int(sys.argv[1])
		if point1 < 1:
			print sys.argv[1] + " is not a positive integer"
			usage()
		if point2 < 1:
			print sys.argv[2] + " is not a positive integer"
			usage()
		
		distance = hex_functions.get_distance_ints(point1, point2)
		print int(distance)