# Backgroud
### Since Leginon uses image shift when collecting images, e.g., 4x4 or 5x5 per batch, we may want to introduce the image shift information from Leginon database into RELION import star file (at the earliest step of data processing), so that we can estimate Beamtilt and do high order aberration correction. In another word, to do better CTF correction by doing high order aberration estimation/correction. This is especially used for intergrating beamtilt group information into RELION 3.1 import star file. 

# Step 1 - Export the Beamtilt information from Leginon

### Login to the leginon computer
- [ ] ssh krios@leginon.niddk.nih.gov
### Go to the "/local/bin/" folder and run the script "get_image_shift_data_all.sh" and name the output file, which contain the image shift information for every image Leginon has taken.
- [ ] cd /local/bin
- [ ]  ./get_image_shift_data_all.sh > leginon_image_shift_data_all_2021-02-04.txt
### And if you view this file, you will be able to see the ID, date, grid name and the image shift information that Leginon generated when taking each image. 
- [ ] more leginon_image_shift_data_all_2021-02-04.txt

<img src="https://github.com/asdstory/Single-Particle-Reconstruction/blob/master/Figures/Leginon_Image_Shift_Information.png?raw=true"
     alt="leginon_image_shift_data from leginon"
     style="float: left; margin-right: 10px;" />

# Step 2 - Just run the program in this way
input the (1)clusters, e.g. 16, or 25 (depends on how you collect the data using Leginon, e.g. 4x4 or 5x5), (2)image shift file, (3)input movies.star file, (4)out movies_group.star file (or any name you like), it will generate a new star file which you can use in later motioncor, CTF correction, 2D 3D etc jobs and turn on the estimate Beamtilt option in Ctfrefine to estimate the beamtilt aberrations.

- [ ] relion_group_image_shift_import_2.py --clusters=25 --image_shift_data=/data/biowulf-data-smb/dout2/DataLibrary/leginon_image_shift_data_all_2021-03_29.txt --input_star=movies.star --output_star=movies_group.star

movies.star file before group looks like 
<img src="https://github.com/asdstory/Single-Particle-Reconstruction/blob/master/Figures/MoviesStarFileBeforeGroup.png"
     style="float: left; margin-right: 10px;"  />
     
movies.star file after group will look like this
<img src="https://github.com/asdstory/Single-Particle-Reconstruction/blob/master/Figures/MoviesStarFileAfterGroup.png"
     style="float: left; margin-right: 10px;" width="400" height="200" />
 
### Jiansen's script will also generate a pdf file showing how good the cluster/group results will be. In general, if you see something like this then it should be fine/the program should work.
- [ ] gvfs-open image_shiftPnuC_20apr27a_g3.pdf

<img src="https://github.com/asdstory/Single-Particle-Reconstruction/blob/master/Figures/Image_shift_cluster%20result%20pdf.png?raw=true"
     alt="run_data_image-shift-grouped-star"
     style="float: left; margin-right: 100px;" />


