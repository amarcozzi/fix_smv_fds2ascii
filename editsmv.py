# This script takes in a .smv file as input, looks for lines with a .q in them 
# (which should only occur when referencing PL3D files)
# And removes the indentation in front of the file name

import fileinput
import sys

def replaceAll(filein, fileout):
     for line in filein:
        if '.q' in line:
            line = line[1:]
        fileout.write(str(line))

if __name__ == '__main__':
    #input = "trails_pl3d.smv"
    #filename, extension = input.split('.')
    filename = sys.argv[1]
    filename, extension = input.split('.')
    with open(input, "r") as filein:
        with open(filename+"_modified."+extension, 'w') as fileout:
            replaceAll(filein, fileout)
