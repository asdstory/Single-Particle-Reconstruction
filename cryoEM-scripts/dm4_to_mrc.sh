#! /usr/bin/env bash

# This script was adopted from https://github.com/Guillawme/cryoEM-scripts/blob/master/dm4_to_mrc.sh.
# Convert a DM4 file from Gatan Digital Micrograph to MRC format.
# EMAN2 needs to be installed and accessible in PATH.

# This line may vary according to your local installation
module load eman2/2.22

DM4=$1
MRC=$2

# If no DM4 or MRC files are provided as command-line arguments, display a short
# usage guide.
if [ $# != 2 ]; then
    echo "Usage: dm4_to_mrc DM4 MRC"
    echo "DM4 is the DM4 file to convert to MRC."
    echo "MRC is the MRC file to save as output (provide a new file name; any existing file would be overwritten!)." 
    exit 0
fi

e2proc2d.py --outtype mrc $DM4 $MRC
