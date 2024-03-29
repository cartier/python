#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This scoring system is application of the DNA testing shown on ERMI test results.  The new roster is designed to help patients (previously sickened by water-damaged buildings) understand if a given building is safe for occupancy. The roster is based on the results of 738 ERMI consecutive test results with 592 that were over 2 and 146 under 2.

We selected five species of fungi from Group I of ERMI based on two criteria.
       1.    Representative of varied water saturations (60-80%; 80-90%; 90-100%).
              a.    Relative risk for enrichment is WDB compared to non-WDB is at least 10 The ratio of incidence in ERMI >2 divided by the Incidence in ERMI <2 must be >10.

We use a point system:
    10 points are awarded for:

        Aspergillus penicilloides     >500 spore E/mg
        Aspergillus versicolor         >500 spore E/mg
        Chaetomium globosum        >125 spore E/mg
        Stachybotrys chartarum   >125 spore E/mg
        Wallemia sebi                     >2500 spore E/mg


    6 points are awarded for    

        A. penicilloides or A. versicolor    >100
        Chaetomium or Stachy                  >25
        Wallemia                                        >500


    4 points awarded for   

        A. penicilloides or A versicolor    >10
        Chaetomium or Stachy                 >5
        Wallemia                                      >100


*Any score over 15 is too dangerous for previously sickened patients to occupy.

*Any score under 11 has been safe to date.

*Any score under 11 has been safe to date.

*Any score 11-15 is borderline. The building must be treated before safety can be assessed.

"""


def hertsmi(ap, av, cg, sc, ws, date):
	score = 0
	if ap > 500:
		score += 10
	elif ap >= 100:
		score += 6
	elif ap >= 10:
		score += 4
		
	if av > 500:
		score += 10
	elif av >= 100:
		score += 6
	elif av >= 10:
		score += 4
			
	if cg > 125:
		score += 10
	elif cg >= 25:
		score += 6
	elif cg >= 5:
		score += 4
		
	if sc > 125:
		score += 10
	elif sc >= 25:
		score += 6
	elif sc >= 5:
		score += 4

	if ws > 2500:
		score += 10
	elif ws >= 500:
		score += 6
	elif ws >= 100:
		score += 4


	print("%-40s   ap = %4d  av = %4d  cg = %4d  sc = %4d  ws = %4d     hertsmi_2 = %4d" % (date, ap, av, cg, sc, ws, score))

# 10/2014  002 cube farm N14403
ap = 7
av = 0
cg = 0
sc = 0
ws = 55
hertsmi(ap, av, cg, sc, ws, "10/2014 002 cube farm N14403")


# 10/2014  002 cube farm N4407
ap = 3
av = 0
cg = 0
sc = 2
ws = 20
hertsmi(ap, av, cg, sc, ws, "10/2014 002 cube farm N4407")




# 2/2014  002 cube farm
ap = 91
av = 64
cg = 2
sc = 12
ws = 110
hertsmi(ap, av, cg, sc, ws, "02/2014 002 cube farm")

# 6/2012 Lexmark 035 1k1
ap = 8
av = 4
cg = 1
sc = 0
ws = 410
hertsmi(ap, av, cg, sc, ws, "06/2012 Lexmark 035 1k1")

# 6/2012 Lexmark 082 
ap = 85
av = 19
cg = 5
sc = 15
ws = 750
hertsmi(ap, av, cg, sc, ws, "06/2012 Lexmark 082")


