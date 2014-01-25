#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

Simply sum up the number of caches in my various KY queries

"""
import re

# open the file

#water_caches_filename = "/home/brian/geocaching/water_caches.txt"
water_caches_filename = "water_caches.txt"

with open(water_caches_filename) as f:
      content = f.readlines()

#print len(content)

cache_count = 0

for line in content:
#      print line
      remat = re.match(r'"(GC.*)",".*","",".*","","(.*)",".*",".*","(.*)",".*",".*",".*",".*",".*",".*",".*",".*",".*",".*",".*",""', line)
      if remat != None:
            gc_number = remat.group(1)
            cache_name = remat.group(2)
            cacher = remat.group(3)
            print "%-7s    %-45s     %s" % (gc_number, cache_name, cacher)
            

