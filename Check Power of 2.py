#function that can determine if an input number is a power of 2

import math
def sqrtt(x):
    i=math.sqrt(x)
    if i**2==x:
        print('the input is power 2 of %s' %(i) )
    else:
        print('it\'s not the power 2')

