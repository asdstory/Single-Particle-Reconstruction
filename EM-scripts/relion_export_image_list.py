#!/usr/bin/env python     

#####**************************************************************************#####
#Despcription: This program is used to move selected micrographs based on .star file.
#Copyright@JiangLab@NHLBI/NIH
#Author: Tongyi Dou
#Last Edit: 2022-01-16
#####**************************************************************************#####

### How to use: python /data/dout2/Scripts/relion_export_image_list.py --input_star Select/job007/micrographs.star --input_source /data/dout2/20210629Krios_rOAT1-LMNG/finished-frames/ --output_destination /data/dout2/20210629Krios_rOAT1-LMNG/Micrographs_selected/


DEBUG=0

import os
import re
import numpy as np
import pandas as pd
import shutil
from optparse import OptionParser
from os import path

np.set_printoptions(threshold=np.inf)

parser = OptionParser()
parser.add_option("--input_star", dest="input_star", type="string", default="", help="Input micrographs.star file generated by RELION [default: %default]")
parser.add_option("--input_source", dest="input_source", type="string", default="", help="Input micrographs.star file generated by RELION [default: %default]")
parser.add_option("--output_destination", dest="output_destination", type="string", default="", help="Input micrographs.star file generated by RELION [default: %default]")


(options, args) = parser.parse_args()


def read_image_list(fn):
    image_list = []
    pattern = r'(\d{8}_\d{8}).mrc'
    for line in open(fn, 'r'):
        line = line.rstrip()
        result = re.search(pattern, line)
        if result:
            image_list.append(result.group(1) + ".tif")
    return image_list

print "Read image list ... "
image_list = read_image_list(options.input_star)
print "Done. %i images were read." % (len(image_list))
#for i in range(len(image_list)):
#    print image_list[i]
    
#list = open("image_list.txt","w")
#for element in image_list:
#    list.write(element + "\n")
#list.close()
#print "Image list is written in the image_list.txt file "


os.mkdir(options.output_destination)
for i in image_list:
    source = options.input_source + i
    destination = options.output_destination + i
    if path.exists(source):
        os.rename(source, destination)
        print("The %s is moved to the location:  %s" %(source, destination))
    else:
        print(source + ": " + "File does not exist.")

    


