def sey_hi():
    print("hi")

def sey_bye():
    print("bye")
import time
sey_hi()
time.sleep(0.3)
sey_bye()
time.sleep(0.3)
sey_hi()
time.sleep(0.3)
sey_bye()
time.sleep(0.3)
sey_hi()
time.sleep(0.3)
sey_bye()

def express_ts(e): #this is a parameter, placeholder for arguement
    return e
expression1=express_ts(1+2)
print(expression1)
expression2=express_ts(45*2)
print(expression2)

def greeter(n):
    return f"Hi {n}!"\
    
first=greeter("jew")
second=greeter("viscosity")
third=greeter("reggin")
print(first,second,third)

def remainder(a,b):
    return a%b
result1=remainder(3,2)
print("remainder:", result1)

def isfar(distance):
    #insert base case
    if distance<0:
       return "error"
    if distance>=100 :
      return "thats far gng."
    elif distance<100 and distance>20:
      return "not too far.."
    elif distance< 20:
      return "its close!"

print(isfar(34)) 
def double_sequencer(n,t):
   value=n
   sequence=[]
  
   for i in range(t):
        value = value * 2
        sequence.append(value)
    
   return sequence

result = double_sequencer(1, 100000)
print(result)

 