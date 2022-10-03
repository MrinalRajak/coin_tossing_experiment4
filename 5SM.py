


# 5:write python code to simulate rolling two dices a million times
# and determine the probability of appearance of same face in
# two successive throws.(Answer should be verified Analitically)



import numpy as np
from random import randint
import random
odds=0
evens=0
trials=1000000
p=0.0

rolling=int(input("How many dise are you going to throw ?: "))
for j in range(rolling):
    result = random.randint(0,5)
        
    #print result
    if result == 0:
        #print "Heads"
        evens += 1
    else:
        #print "Tails"
        odds += 1
    
print ("The result is: ")
print ("Evens: ",evens)
print ("Odds: ",odds)
