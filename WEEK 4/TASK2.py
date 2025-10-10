# Program starting message
print("Program starting.\n")

# Ask user for starting and stopping values
start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))

print("\nStarting for-loop:")

# Use for-loop to print numbers on the same line
for i in range(start, stop + 1):  # +1 to include the stopping value
    if i < stop:
        # Print number followed by a space (no new line)
        print(i, end=" ")
    else:
        # For the last number, print without extra space
        print(i, end="")

# Print ending message
print("\n\nProgram ending.")
