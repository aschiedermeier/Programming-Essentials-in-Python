# 5.1.2.5 Useful Modules | random

from random import random, seed

for i in range(5):
    print(random())
    
seed(0)

for i in range(5):
    print(random())
    
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))


from random import choice, sample
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(lst))
print(sample(lst, 5))
print(sample(lst, 10))