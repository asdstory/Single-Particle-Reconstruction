#!/bin/bash
mkdir select_micrographs

#print select micrographs to select.txt
#awk '/MotionCorr\/job(\d{3})\/Micrographs\/(\d+_\d+).mrc/ {print $1}' ./micrographs.star > select.txt
#awk '/MotionCorr\/job[0-9]+\/Micrographs\/([0-9]+_[0-9]+).mrc/ {print $1}' ./micrographs.star > select.txt
#awk 'match($0, /MotionCorr\/job[0-9]+\/Micrographs\/([0-9]{8}_[0-9]{8}).mrc/, a) {print a[1]}' ./micrographs.star > select.txt
awk '/MotionCorr\/job011\/Micrographs\/FoilHole_[0-9]+_Data_[0-9]+_[0-9]+_[0-9]+_[0-9]+_Fractions.mrc/ {print $1}' ./micrographs.star > select.txt
#awk -F "[/_.]" '/^MotionCorr/{print "dosef_quick_png/" $4 "_" $5 "_CorrSum.png" "\n" "dosef_quick_png/" $4 "_" $5 "_CorrFFT.png"}' Select/job010/micrographs.star > selec$

#copy select micrographs to folder select_micrographs
cat select.txt | while read line
do
       filename=`basename $line`;
       echo $filename;
       filename+='.tif';
       cp $line select_micrographs;
done


