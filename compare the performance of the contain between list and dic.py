import timeit
import random
from timeit import Timer

"""
"Problem solving with Algo. and DS" compare the performance of the contains operation between lists and dictionaries. 
the contains operator for lists is 𝑂(𝑛) and for dictionaries is 𝑂(1). 
make a list with a range of numbers in it. Then pick numbers at random and check to see if the numbers are in the list. 
"""

for i in range(1000000,1000,40000):
    t = Timer("random.randrange(%d) in x"%i,"from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    dic_time = t.timeit(number=1000)
    
print("%d,%10f,%10f" % (i, lst_time, dic_time))

