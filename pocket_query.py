#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

Simply sum up the number of caches in my various KY queries

"""
import re

# open the file

with open("/home/brian/geocaching/ky_queries.txt") as f:
      content = f.readlines()

#print len(content)

cache_count = 0

for line in content:
#      print line
      remat = re.match(r'.*# (\d+)', line)
      if remat != None:
            cache_count += int(remat.group(1))
            print "add %d" % int(remat.group(1))

print cache_count

