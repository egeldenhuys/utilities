#!/bin/python

# Usage:
#   rename.py <directory>

# Get List of files
# Human sort files
# Rename files, adding prefix counter

import sys
import os
from os import listdir
from os.path import isfile, join
from natsort import natsorted, ns

directory = sys.argv[1]

# https://stackoverflow.com/a/3207973
files = [f for f in listdir(directory) if isfile(join(directory, f))]
files = natsorted(files, alg=ns.IGNORECASE)

count = 1

for f in files:
    countString = str(count)

    if count < 10:
        countString = '0' + countString
    
    newFileName = join(directory, countString + ' ' + f)
    os.rename(join(directory, f), newFileName)
    count += 1

    print(newFileName)
