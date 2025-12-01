from A8_T2_lib import add, subtract, multiply, divide

def showOptions():
    print("Options:\n1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide\n0 - Exit")

def askChoice():
    return input("Your choice: ")

def askValue(prompt):
    return float(input(prompt))

def main():
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        if choice == "1":
            a = askValue("Insert first addend value: ")
            b = askValue("Insert second addend value: ")
            print(f"{a} + {b} = {add(a,b)}")
        elif choice == "2":
            a = askValue("Insert minuend value: ")
            b = askValue("Insert subtrahend value: ")
            print(f"{a} - {b} = {subtract(a,b)}")
        elif choice == "3":
            a = askValue("Insert multiplicand value: ")
            b = askValue("Insert multiplier value: ")
            print(f"{a} * {b} = {multiply(a,b)}")
        elif choice == "4":
            a = askValue("Insert dividend value: ")
            b = askValue("Insert divisor value: ")
            print(f"{a} / {b} = {divide(a,b)}")
        elif choice == "0":
            print("Exiting program.\nProgram ending.")
            break
        else:
            print("Unknown option!")

main()
