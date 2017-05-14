#!/usr/bin/python


"""Print lat/long in DD MM.MMM format given decimal degrees"""

import sys
def printf(format, *args):
    sys.stdout.write(format % args)


import sys

def usage():
  print sys.argv[0] + " : Print lat/long in DD MM.MMM format given decimal degrees.\n"
  print "Usage:" + sys.argv[0] + " xx.xxxxxx, yy.yyyyyy\n"
  print "\n\n"
  sys.exit(1)

if len(sys.argv) != 3:
  usage()
else:
  lat = sys.argv[1]
  if len(lat) > 0:
    if lat[-1:] == ",":
      lat = lat[:-1]

lon = sys.argv[2]

lat = float(lat)
lon = float(lon)

if (lat > 0):
  cardinal_lat = 'N'
else:
  lat = -lat
  cardinal_lat = 'S'

if (lon > 0):
  cardinal_lon = 'E'
else:
  lon = -lon
  cardinal_lon = 'W'

latdeg = int(lat)
latmin = (lat - int(lat)) * 60

londeg = int(lon)
lonmin = (lon - int(lon)) * 60


printf("\n%c %2d %02.3f %c %03d %02.3f\n\n", cardinal_lat, latdeg, latmin, cardinal_lon, londeg, lonmin)
