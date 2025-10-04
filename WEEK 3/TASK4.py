print("Program starting.")
print("This is a program with a simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")
print("")

print("Options:")
print("1 - Welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character of the name")
print("4 - Show the amount of characters in the name")
print("0 - Exit")

Feed = input("Your choice: ")
Choice = int(Feed)

if Choice == 1:
    print(f"Welcome {name}!")
elif Choice == 2:
    print(f"your name backward is {name[::-1]}")
elif Choice == 3:
    print(f"The first character in name {name} is {name[0]}")
elif Choice == 4:
    print(f"There are {len(name)} characters in the {name}")
elif Choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("Program ending.")    
          
