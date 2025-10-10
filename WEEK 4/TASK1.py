#🧩 Step-by-step guide:

#Start your program with a print statement
#Print a message like “Program starting.” to show the beginning of the program.
print("Program starting.")

#Ask the user for input
start_value = int(input("Enter a starting value: "))
stop_value = int(input("Enter a stopping value: "))

#Show that the loop is starting
print("Starting for-loop:")

#Use a for loop
#Use the range() function with your starting value and stopping value
for i in range(start_value, stop_value + 1):
    #Inside the loop, print each number
    print(i)

#After the loop ends, print “Program ending.” to show completion.
print("Program ending.")