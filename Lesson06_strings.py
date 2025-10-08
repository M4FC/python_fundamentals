greeting="hello"
name="ada"
print(greeting,name)


message=greeting + " " + name + "!!!!"
print("concatenated message", message)
second=greeting[1]
print(second)

wrd="supercalifragilisticesxplalidocious"
print("first letter", wrd[0])
print("last letter", wrd[-1])
print("range of letters(non-inclusive):", wrd[-7:-2])
print( wrd [:5] )
print( wrd [2::4])
print( wrd [-7:])
print(wrd[:-7])
print("step through every second character:" , wrd[::2])
print("smth", wrd [3:6:2])
country="ecuador"
length_of_word=len(country)
print(length_of_word)
random_phrase="SiX SEvEn!"
print("\nUppercase:", random_phrase.upper())
print("\nlowercase:", random_phrase.lower())
print("\ncapitalize:", random_phrase.capitalize())

#find and replace text
sent="im a goofy goober"
new=sent.replace("im","your")
print(sent)
print(new)


#formatted strings
print("\n---formatted strings--- ")
name="ada"
age=28
city="London"
print(f"hello, my name is {name}. I am {age} years old and live in {city} ")
print(f"next year ill be {age+1}, and my name uppercase is{name.upper()}")

#challenge 1
quote=input("what is ur favorite quote")
print("your favorite quote is",len(quote))
#challenge 2
first=(input("what is your first name"))
last=(input("what is your last name"))
print(last,first)

#challenge 3
A_word=(input("gimme a word plox"))
print(A_word.upper())
print(A_word.lower())
print(A_word[])








