#!/usr/bin/python
# -*- coding: utf-8 -*-

"""



Solve Paul's DNA cache puzzle

"""

# I saw a paper about encoding dna.  They used A and C for zero.
# However, the data set here appears to have A and T be zero IFF the values are in the lower 127 ascii range.

def get_bin (ch):
      if (ch == 'A' or ch == 'T'):
            return 0
      elif (ch == 'G' or ch == 'C'):
            return 1
      else:
            print "ERROR - not a valid letter"
            return 0


def get_int_dna (str):
      value=0
      for ch in str:
            value <<= 1;
            value += get_bin(ch)

      return value



#test = 'TCGACGCG'
#print (get_int_dna(test))


dna_list =(
'ACATCCGT',
'TCGACGCG',
'ACCGTTGA',
'TCGCACAA',
'AGGTGTTT',
'TTGTTAAA',
'TACCTAGG',
'TACCCATA',
'ACAATCTT',
'AGGAAGTG',
'AGCAACCG',
'AAGCATAT',
'AAGGTAAC',
'TCATCGAC',
'TCCAGTAG',
'TGCACCCA',
'TACGTGAT',
'TTGCAATT',
'TACAGGGA',
'TTGGAACG',
'ACTCATCG',
'TCCATGTG',
'TGGATTGG',
'AAAACCAG',
'TAAACACT',
'TCTCACCC',
'ACCTACAG',
'TCGGTTCG',
'TCGCTGAA',
'TTCCGATA',
'TAGGTCTA',
'ACATTGAT',
'TCGTACTG',
'AGGTTGCG',
'TTCATTTT',
'AAGCTTCA',
'TTGGAGTC',
'TGATGCAC',
'TCCTGAAG',
'TCCAGCCA',
'AACGTCAC',
'ATGGGTAT',
'ATGAGCGA',
'TTCGTATC',
'ACTCATCC',
'AGGTAGAC',
'AGCAATGC')



#print (get_int_dna(test))

newstr=""
for str in dna_list:
      newstr += chr(get_int_dna(str))

print (newstr)




