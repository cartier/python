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
      remat = re.match(r'.*(\d{1,2}/\d/\d{4,4}).*(\d{1,2}/\d/\d{4,4}).*# (\d+)', line)
      if remat != None:
            start_date = remat.group(1)
            end_date = remat.group(2)
            cache_num = int(remat.group(3))
            cache_count += cache_num
            print start_date, end_date, cache_num


print cache_count

