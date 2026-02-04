# CHAL 1
def addition(n,j):
    return n+j
def subtraction(W,L):
    return W-L
def multiplication(h,m):
    return h*m
def division(y,s):
    return y/s
test1=addition(45,7)
print(test1)

#chal 2

def average(n,l,t):
     return (n+l+t)/3
test=average(1028,82,573)
print(test)


#chal 3
def is_even(n):
    return n%2
answer=is_even(9)
if answer==1:
 print("odd")
elif answer==0:
    print("even")
else:
    print("error")

#chal 4
def analyze_word(word):
    if type(word) is not str:
        return "error"
    vowels=0
    constanants=0
    for char in word:
        if char in ["i","e","u","o","a"]:
            vowels+=1
        else:
            constanants+=1
    return f"{vowels} vowels,{constanants} constanents"
print(analyze_word("wilderness"))


  