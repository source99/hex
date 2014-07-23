#!/usr/bin/env python
#
# Image skip based on:
# http://stackoverflow.com/a/4614629
#

import ImageFile
import struct
import binascii
import sys
import os
import re
import glob

# Regexp to sanitize filenames (remove path separators, etc.)
_split = re.compile(r'[\0%s]' % re.escape(''.join(
    [os.path.sep, os.path.altsep or ''])))

def sanitizeFilename(path):
    return _split.sub('', path)

def getImageHeader(fp, start):
    fp.seek(start, 0)
    fp.seek(-23, 1)
    return sanitizeFilename(fp.read(23))

def getImage(fp, start, end, save_folder):
    # Get image header to use as filename later
    #print "getting {} bytes from {} to {}".format(end-start, start, end)
    imgHeader = getImageHeader(fp, start)

    # Seek to start of image, read until end of image
    fp.seek(start, 0)
    imData = fp.read(end - start)
    
    # Decode this image as a JPEG using PIL
    try:
        p = ImageFile.Parser()
        p.feed(imData)
        im = p.close()
         # Saves image in current directory using timestamp
        im.save("{}/hires/{}.jpg".format(save_folder,imgHeader))
    except IOError as err:
        print "frame {} is not a jpeg".format(imgHeader)


def getImages_directory(directory, save_folder):
    print "directory = {}".format(directory)
    files = glob.glob("{}/HiRes/*/*/*.sjp".format(directory))
    print "files = {}".format(files)
    for filename in files:
        getImages(filename, save_folder)
    return



def getImages(filename, save_folder):
    # Load up image file
    fp = open(filename, "rb")
    p = ImageFile.Parser()

    # Confirm that file has correct "header"
    #header = fp.read(11)
    #if header != "Ver:003.000":
        #raise ValueError("File has unknown type: {0}".format(header))

    # Store EOF position
    fp.seek(0, 2)
    eof = fp.tell()
    fp.seek(11, 0)

    # Parse file for JPEG images
    d = '\x00'
    while len(d) > 0:
        # Search for JPEG start marker
        d = fp.read(1)
        if d != '\xFF':
            continue

        d = fp.read(1)            
        if d != '\xD8':
            continue
    
        # Record start position of image
        start = fp.tell() - 2
    
        while len(d) > 0:
            # Seek next marker in image
            d = fp.read(1)
            if d != '\xFF':
                continue

            # Handle marker type (seek past if unknown or, decode if end tag)
            d = fp.read(1)
            if d == '\x00' or d == '\x01' or (d >= '\xD0' and d <= '\xD8'):
                continue
            elif d == '\xD9':
                end = fp.tell()
                #sys.stdout.write("\rProgress: {0:6.2f}%".format(100.0 * end / eof))
                #sys.stdout.flush()
                getImage(fp, start, end, save_folder)
                break
            else:
                skipStr = fp.read(2)
                skipLen = struct.unpack('>H', skipStr)[0] - 2
                fp.seek(skipLen, 1)

    fp.close()


def usage():
    name = sys.argv[0] or "imagery.py"
    print('Usage: {0} [datafile (.sjp or .mci)]'.format(name))
    print('\tdatafile - name of image data file')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    else:
        #arg1 = source directory
        #arg2 = run directory
        getImages_directory(sys.argv[1], sys.argv[2])
