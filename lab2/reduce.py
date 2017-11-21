#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
#import numpy

#number of columns of A/rows of B
n = int(sys.argv[1]) 

#Create data structures to hold the current row/column values (if needed; your code goes here)

currentkey = None
dictA = []
dictB = []
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	#Remove leading and trailing whitespace
	line = line.strip()

	#Get key/value 
	key, value = line.split('\t',1)

	#Parse key/value input (your code goes here)
        stripped = value.strip('[]\n')
        name, i, value = stripped.split(',') 

	#If we are still on the same key...
	if key==currentkey:

		#Process key/value pair (your code goes here)
           if name == "'A'":
              dictA.append(float(value))
           if name == "'B'":
              dictB.append(float(value))

	#Otherwise, if this is a new key...
	else:
		#If this is a new key and not the first key we've seen
		if currentkey:

		    	#compute/output result to STDOUT (your code goes here)
	            res = 0
                    for i in range(len(dictA)):
                        temp = dictA[i]*dictB[i]
                        res += temp
                    dictA = []
                    dictB = []
                    print '%s\t%s' % (currentkey, res)

	
		currentkey = key
		
		#Process input for new key (your code goes here)
                if name == "'A'":
                   dictA.append(float(value))
                if name == "'B'":
                   dictB.append(float(value))      

#Compute/output result for the last key (your code goes here)
res = 0
for i in range(len(dictA)):
    temp = dictA[i]*dictB[i]
    res += temp
print '%s\t%s' % (key, res)



