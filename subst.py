#!/usr/bin/python
import sys, re, os, glob

# will search for all files Resources_*.properties and replace \n with a space only on the line 
#sbmymfp.welcomeScreenCustomizerTitle

filelist = glob.glob("Resources_*.properties")

for filename in filelist:
    infile = open(filename, 'r')

    linelist = []

    for line in infile:
        linelist.append(re.sub(r'(usbmymfp.welcomeScreenCustomizerTitle.*?)(\\n)(.*)', r'\1 \3\n', line))

        
    infile.close
    outfile = open(filename, 'w')

    for line in linelist:
        outfile.write(line)

    outfile.close


