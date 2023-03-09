#!/usr/bin/env python     

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
parser.add_option("--output_star", dest="output_star", type="string", default="", help="Input micrographs.star file generated by RELION [default: %default]")


(options, args) = parser.parse_args()

def read_image_list(fn):
    image_list = []
    pattern = r'\S*\w*\.mrcs'
    for line in open(fn, 'r'):
        line = line.rstrip()
        result = re.search(pattern, line)
        if result:
            image_list.append(result.group(0))
    return image_list

image_list = read_image_list(options.input_star)

'''
for i in range(len(image_list)):
   print (image_list[i])
'''

f_out = open(options.output_star, "w")

'''
for i in range(len(image_list)):
   f_out.write(image_list[i])
   f_out.write("\n")
'''
    
with open(options.input_source) as f:
    for line in f:
        if not line.startswith((' 0',' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9')):
            print (line)
            f_out.write(line)
'''            
        for i in range(len(image_list)):
            if image_list[i] in line:
#                print (line)
                f_out.write(line)
                break
'''                
f_out.close() 

'''
for i in range(len(new_list)):
    print (new_list[i])
    print ("There are in total" + len(new_list) + "particles selected" + "\n")
'''  
#list = open("image_list.txt","w")
#for element in image_list:
#    list.write(element + "\n")
#list.close()
#print "Image list is written in the image_list.txt file "


