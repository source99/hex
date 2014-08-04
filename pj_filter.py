import sys
import os
import glob
import multiprocessing as mp
import subprocess


def process_range(file_list,start,stop):
    for i in range(start,stop):
        filename = file_list[i]
#        print filename
        head,tail = os.path.split(filename)
        #print "parts = {} {}".format(head, tail)
        new_name = "{}{}nobg-{}".format(head,os.sep,tail)

        #command = "\"C:\Program Files\ImageMagick-6.8.9-Q16\convert.exe\" -posterize 2 -fill white -opaque black -colors 2 {} {}".format(filename,new_name)
        command = "\"C:\Program Files\ImageMagick-6.8.9-Q16\convert.exe\" -posterize 2 -fill white -opaque black -colors 2 {} -median 6 {}".format(filename,new_name)
        subprocess.call(command)



if __name__ == "__main__":
    if len(sys.argv) < 3 and False:
        print "you're doing it wrong"
    else:
        file_list = glob.glob("laser/camall/rectified/2*.png")
        num_cores = 15
        num_images = len(file_list)
        images_per_core = num_images / num_cores
        jobs = []
        for i in range(0,num_cores-1):

            start_image = i * images_per_core
            stop_image = (i+1) * images_per_core
            print "starting {} {} {}".format(i,start_image, stop_image)
            p =  mp.Process(target=process_range,args=(file_list,start_image,stop_image) )
            jobs.append(p)
            p.start()
        i = num_cores-1
        start_image = i * images_per_core
        stop_image = len(file_list)
        p =  mp.Process(target=process_range,args=(file_list,start_image,stop_image) )
        jobs.append(p)
        p.start()

        for j in jobs:
            j.join()



