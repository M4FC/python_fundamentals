#conditionals
print(4!=2)
#if
num=12
if num==12:
   print("your number is 19")

num2=12
print(num2<=10)
if num2<=19:
 print("chemga")
 
 temperture=59
 if temperture > 80:
   print("its hot")
 elif temperture >= 60:
    print("its nice")
 else:
   print("its cold")
x=20
y=20
if x==y:
  print("x is equal to y")
elif x>y:
  print("x is greater than y")
elif x<y:
  print("x is less than y")
else:
  print("error")


age= 17
has_permission=False
if age>= 17 and has_permission:
  print("you can drive")
else:
  print("u cant drive")
  # when using and statement both have to be true

  # or 

  day="tuesday"

  if day=="saturday" or day=="sunday":
    print("it's the weekend")
  elif day=="monday" or day=="tuesday":
    print("its the start of the weekday ")
  else:
   print("its the weekday")

  if day is not "monday":
    print("its not monday")

# review challenges 

#challenge 1: even or odd challenge
number=int(input("gimme a number plox"))
output=number%2
print(output)
if output==0:
  print("Your number is even")
else:
  print("your number is odd")


#challenge 2: password check
Password=input("enter password")
real_password="smegmacheese25"
if Password==real_password:
  print("access granted")
else:
  print("access denied")
nextattempt=input("try again")
if Password== real_password:
  print("access granted")
else:
  print("locked out")

#challenge 3:grading system
Grade=int(input("enter numeric grade"))
if Grade<=60:
  print("F")
elif 60<=Grade<70:
  print("D")
elif 70<=Grade<80:
  print("C")
elif 80<=Grade<90:
  print("B")
elif 90<=Grade<=100:
  print("A")





    
    


