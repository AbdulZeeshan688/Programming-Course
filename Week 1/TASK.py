#Hello, this is not printed, because it is a comment. 
name = "Zeeshan" # This is not shown 
print ("Hello world!",name) 
print ("I'm in finland")

print("He said :\"hello!\" and kept waling ")
print ("He said Hello\\' and kept waling")

#input ("What is your name ?")
#print("welcome"+ input ("what is your name")+ "!")

name = input ("what is your name")
print (f"Welcome {name}!")

Sentence= "Find a substring"
print(Sentence)# Print the whole sentence 
print (Sentence[2]) # prints the...
print (Sentence[-2])# Print the...
print(Sentence[2:9])
print (Sentence[:9])
print (Sentence[-9:-2])
print (Sentence[2:9:3])
print (Sentence[::3])
print (Sentence[::-1])

exString = "Hello"
exInt = 2 
exBool = 3.14 


print(123 +456)
num1 = input ("Give me a number")
num2 = input ("Give me another number")
print(int(num1) + int(num2))

calclength = len (Sentence)

num3 = 10 
num4 = float(num3)

print(5 * 3 - 4/ 2 + 2)
print(5 * 3 -4/(2+2 ))
# roundMe =

#Using % formating 
Name = "Zeeshan g"
Age = 20 
Formatted = "My name is %s and I am %d year old." %(Name, Age)
print(Formatted)

# %s = placeholder for a string 
# %d = placeholders for a intger 

# Figer out what is the placeholder for float when using % formatting 

#Using format () method 
Formatted2 = "My name is [0] and I am [1] year old." .format(Name, Age)
print(Formatted2)

RoundThis = 5.345353534
print("{:.2f}").format(RoundThis)