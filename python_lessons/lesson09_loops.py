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



