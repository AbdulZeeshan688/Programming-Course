print("Program starting:")

num1 = int(input("Insert starting value:"))
num2 = int(input("Insert stopping value:"))
num3 = int(input("Insert inspection value:"))

if num1<num2 and num1<=num3<=num2:
    print("First loop - inspection with break:")
    for i in range(num1, num2):
        if i == num3:
            break
        print(i, end=" ")
    print()

    print("Second loop - inspection with continue:")
    for i in range(num1, num2):
        
        if i == num3:
            continue 
        print(i, end=" ")
    print()

if (num1 == num2 and num3>num2):
    print("Starting point value must be less than the stopping point value.")
    if (num3<num1 or num3>num2):
        print("Inspection value must be within the range of start and stop.")

elif (num3<num1 or num3>num2):
    print("Inspection value must be within the range of start and stop.")



print("Program ending.")f