#USER INPUT IN PYTHON
import math
name=input("enter your name:")
print("hello", name)
age= input("enter your age")
print(type(age))

age_number= int(age)
print("Next year you will be ", age_number + 1 )
print(type(age_number))

Height=float(input("enter your height"))
print("you are", Height ,"meteres tall")

#challenge 1
Color=input("state your favorite color")
print(Color,"is a great color")

#challenge 2
import math

Number1=(input("enter any number"))
Number2=(input("enter any number again"))
number1=int(Number1)
number2=int(Number2)
print(Number1,"plus", Number2,"equals", number1+number2)
#challenge 3
Diameter=float(input("state a number 4 diameter"))
radius=Diameter/2
print(radius)
print("circle with this diameter is", math.pi*radius**2)




# challenge 4
import random
die=int(input("how many sides"))
die_roll= random.randint(1,die)
print(die_roll)
