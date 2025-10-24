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
replace= animals.index("dolphin")
animals[replace]="seamonkey"
print(animals)

nums= [3,38,0,2,12,67,41,24]
print("og numbers:", len(nums),"numbers")
print("minimum value is:",min(nums))
print("max value is:",max(nums))
print("sum is:",sum(nums))
nums.sort()
print(nums)
"AAAAHH"
animals.sort()
print(animals)

if "cat" in animals:
    print("cat is in list")
else:
    print("cat isn't in the list")


og_list=[3,2,1]
copied_list= og_list.copy()
print(og_list)
print(copied_list)
copied_list.append(4)
print(og_list)
print(copied_list)



#challenge 1
chal_list=[1,2,3,4,5,6]
newnum=int(input("insert a number"))

new=chal_list.index(3)
chal_list[new]=newnum
print(chal_list)

#challenge 2








