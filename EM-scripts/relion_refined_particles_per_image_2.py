#!/usr/bin/env python     

#####***************************************************************************************************#####
#Despcription: This program is used to prepare the .order file for RELION subtomogram averaging.
#Author: Tongyi Dou
#How to use: "relion_prepare_orderfile.py --i run_data.star --o refined_particles_per_image.csv"
#Test data: data = [[20210527_05260821,200,3.53,2.09], [20210527_05070268,190,3.42,1.39],[20210525_23585333,180,3.17,1.65]]
#Last Edit: 2021-08-22
#####***************************************************************************************************#####


import re
import numpy as np
import pandas as pd
from optparse import OptionParser

np.set_printoptions(threshold=np.inf)

parser = OptionParser()
parser.add_option("--i", dest="input_star", type="string", default="", help="Input .star file generated by RELION Refine3D or Class3D job [default: %default]")
parser.add_option("--o", dest="output_list", type="string", default="", help="Output .csv file with particles per image count [default: %default]")

(options, args) = parser.parse_args()

def count_particle_per_image(file_i,file_csv):
    dictionary = dict()
    data = []
    pattern = r'(\d{8}_\d{8}.mrc\b)'
    for line in open(file_i, 'r'):
        line = line.rstrip()
        result = re.search(pattern, line)
        if result:
            image_name = result.group(1)
            if image_name in dictionary:
                dictionary[image_name] +=1
            else:
                dictionary.update({image_name:1})
            list = line.split()
            defocus = float(list[11]/10000)
            data.append([image_name,dictionary[image_name],list[9],defocus)
    print(data)
    df = pd.DataFrame(data,columns = ['Image Name','Refined Particles','Resolution(A)','Defocus(um)'])
    df = df.sort_values(by = 'Refined Partciles',ascending=False)
    print(df)
    df.to_csv(file_csv,index=False)
    
count_particle_per_image(options.input_star,options.output_list)

