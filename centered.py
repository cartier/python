#!/usr/bin/python
# -*- coding: utf-8 -*-

"""



compute the geometric centroid in a piecewise fashion

"""



import math



cx = 0.0
cy = 0.0
totalarea = 0.0



def showcentroid(totalarea, cx, cy):
	print "totalarea = %f    (cx, cy) : (%f, %f)\n" % (totalarea, cx, cy)
	print "(centroid) = (%f, %f)\n" % (cx/totalarea, cy/totalarea)
        x = cx/totalarea
        y = cy/totalarea
        print "magnitude: %g" % math.sqrt(x*x + y*y)


def addcentroid(area, centerx, centery):
        global totalarea
        global cx, cy
	totalarea += area
        

	cxx = centerx * area
	cyy = centery * area

        print "(area, cxx, cyy) : (%f, %f, %f)" % (area, cxx, cyy)

	cx += cxx
	cy += cyy
        showcentroid(totalarea, cx, cy)
	




# add big rectangle
area = 3 * 2.5
centerx = 1.5
centery = 2.5/2
addcentroid(area, centerx, centery)


# subtract small circle
area = - math.pi * math.pow(0.25, 2)
centerx = 0.5  # note minus sign since this section is a hole
centery = 0.5
addcentroid(area, centerx, centery)

# subtract large semicircle
area = - 0.5 * math.pi * math.pow(0.75,2)
centerx =  2
centery =  4 * 0.75 / (3 * math.pi)
addcentroid(area, centerx, centery)

# subtract small rectangle
area = - 0.5 * 1.5
centerx = 1.25
centery = 1.75
addcentroid(area, centerx, centery)

# subtract triangle
area = - 0.5 * 1.5 * 1
centerx = (3 - 1/3.0)
centery = (2.5 - 0.5)
addcentroid(area, centerx, centery)


print "totalarea: ",totalarea

x = cx / totalarea
y = cy / totalarea


theta = math.atan(y/x)
theta += math.pi/2



angle = math.degrees(theta)

print x,y,angle
print x*5280, y*5280

dist = math.sqrt(x *x + y*y)
print dist

print "%g miles at %f degrees" % (dist, angle)
print "%g feet at %f degrees" % (dist * 5280, angle)
