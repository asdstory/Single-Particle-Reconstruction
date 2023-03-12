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
f_out = open(options.output_star, "w")

dict = {}
with open(options.input_source) as f:
    for i,line in enumerate(f):
        if i > 58:
            for j in range(len(image_list)):
                if image_list[j] in line:
                    dict[image_list[j]] = line
                    break
                    

with open(options.input_source) as f:
    for i,line in enumerate(f):
        if i <= 58:
            f_out.write(line) 
        else: 
            break

for i in range(len(image_list)):
    f_out.write(dict[image_list[i]])
    break
               
f_out.close()                
'''
                    
                    
'''
f_out = open(options.output_star, "w")

with open(options.input_source) as f:
    for line in f:
        if '@' not in line:
            f_out.write(line)            
        for i in range(len(image_list)):
            if image_list[i] in line:
                f_out.write(line)
                break
               
f_out.close() 
'''

'''
f_out = open(options.output_star, "w")

with open(options.input_source) as f:
    for i,line in enumerate(f):
        if i <= 58:
            f_out.write(line) 
        else: 
            for j in range(len(image_list)):
                if image_list[j] in line:
                    f_out.write(line)
                    break
               
f_out.close() 
'''

