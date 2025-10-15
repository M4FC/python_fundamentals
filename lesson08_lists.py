#lists in python
#lists store multiple values in one variable
#they are ordered, mutable(changeable), and allow duplicates
animals=["donkey", "dolphin", "blobfish"]
numbers=[1,4,3,9,0]
mixed=["miggle", 67 , "cracked windshield"]
print(animals)
print(numbers)
print(mixed)
print()
print("first element:", animals[0])
print()
print("last element:", animals[-1])
#modifying lists
animals[0] ="babariusa"
print()
print(animals)
animals.append("glass frog")
print()
print(animals)
# insert elemnet in specific index
animals.insert(2,"aye-aye")
print()
print(animals)
animals.insert(1, "camel")
print()
print(animals)
animals.remove("aye-aye")
print()
print(animals)
last_animal=animals.pop()
print(last_animal)
print(animals)
# useful lists functions
