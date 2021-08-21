#!/usr/bin/env python     

#####**************************************************************************#####
#Despcription: This program is used to search and replace pattern in .star file.
#Author: Tongyi Dou
#How to use: Just "python replace.py --i run_data.star --o run_data_replace.star"
#Last Edit: 2021-07-02
#####**************************************************************************#####


import re
import numpy as np
from optparse import OptionParser

np.set_printoptions(threshold=np.inf)

parser = OptionParser()
parser.add_option("--input_tlt", dest="input_tlt", type="string", default="", help="Input .tlt file generated by IMOD [default: %default]")
parser.add_option("--input_mdoc", dest="input_mdoc", type="string", default="", help="Input .mdoc file generated by SeiralEM [default: %default]")
parser.add_option("--o", dest="output_order", type="string", default="", help="Output .order file used for RELION subtomogram averaging [default: %default]")

(options, args) = parser.parse_args()

def extract_refined_tilt_angle(file):
    # Read contents from file as a single string
    file_i_handle = open(file_i, 'r')
    file_i_string = file_i_handle.read()
    file_i_handle.close()

    # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
    file_i_string = (re.sub(pattern, subst, file_i_string))

    # Write contents to file.
    # Using mode 'w' truncates the file.
    file_o_handle = open(file_o, 'w')
    file_o_handle.write(file_i_string)
    file_o_handle.close()
def extract_accumulated_dose(file):
    
def write_order_file(file):
    
extract_refined_tilt_angle(options.input_tlt)
extract_accumulated_dose(options.input_mdoc)
write_order_file(options.output_order)
    
    
pattern = r'(\d{3})_(\d{2})\.(\d{2})\.(\d{2})\.mrc'				
subst = r'\1_\2_\3_\4.mrc'	


