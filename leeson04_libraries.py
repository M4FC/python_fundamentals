import math
print("\n--- Math Library ---\n")

print("square_root:",math.sqrt(25))
print("round up:",math.ceil(4.6))
print("round down:",math.floor(4.6))
print("pi:", math.pi)

#RANDOM LIBRARY
seed=23829
cs_EST=45
print(seed*cs_EST)
nextprt=seed*cs_EST/(seed/2*cs_EST)
print(nextprt)
print("round up:", math.ceil(nextprt))

import math

seed= 123.45
step1= seed/6.7
print(step1)
step2=step1-800
step3=step2 + 180843
step4=step3 % 10
result= math.floor(step4)
print(result)

import random

#methods
print("Random integer: ", random.randint(1, 100))
print(random.random())

mylist=["eggs","cheese","smegma"]
print(random.choice(mylist))
random.shuffle(mylist)
print(mylist)


#challenge 1
import math
radius=7
circle_area= math.pi*7**2
print(circle_area)

#challenge 2
Die_roll=random.randint(1,6)
print(Die_roll)








