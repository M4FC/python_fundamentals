#loops
#two types of loops, for and while loops


#for loops
#repeats itself for each element in a sequence
import time
animals=["lamb", "sheep", "cow", "goose", "donkey"]
animals[0]
for animal in animals:
    print("now petting a", animal)
    time.sleep(1.5)
    if animal =="sheep":
      print("Hi sheep")
print("\nnow I have pet all the animals :)")


for i in range(2,11,2):
   print("counting evens", i)


count=1
while count < 5: 
    print(f"Loopin'. We are on loop # {count}.")
    count += 1
    time.sleep(0.5)

print("We have escaped the loop!")

user_input = ""

while user_input != "exit":
    user_input = input("Type 'exit' to escape:")

count = 60
increment = 1

while count > 0:
    count -= increment
    increment += 1
        
    if count < 0:
        break

    print(count)
    
    
  
  
   


