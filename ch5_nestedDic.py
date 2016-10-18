#! python3
#ch5_nestedDic.py is an example of nexted dictionaries

import time
allguest = {'pedro':{'apples':4,'pears':1,'grapes':3},
'paola':{'oranges':2,'pears':3,'water':4},
'perla':{'raspberry':3,'apples':6,'oranges':2},
'rodrigo':{'greaps':3,'water':9,'raspberry':7}}

def printFood(guestDic, product):
    numProducts = 0 
    for k, v in guestDic.items():
        numProducts += v.get(product,0)
    return numProducts

print ('number of things brough')
print ('apples'.ljust(20, '.') + str(printFood(allguest, 'apples')).rjust(5))
print ('pears'.ljust(20, '.') + str(printFood(allguest, 'pears')).rjust(5))
print ('grapes'.ljust(20, '.') + str(printFood(allguest, 'grapes')).rjust(5))
print ('raspberry'.ljust(20, '.') + str(printFood(allguest, 'raspberry')).rjust(5))
print ('water'.ljust(20, '.') + str(printFood(allguest, 'water')).rjust(5))
time.sleep(7)
