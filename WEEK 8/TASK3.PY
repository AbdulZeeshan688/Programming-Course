def main():
    values = []
    print("Program starting.")
    while True:
        print("Options:\n1 - Read values\n2 - Amount of values\n3 - Calculate sum of values\n4 - Calculate average of values\n0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            filename = input("Insert filename: ")
            with open(filename) as f:
                values = [float(line.strip()) for line in f if line.strip()]
        elif choice == "2":
            print(f"Amount of values {len(values)}")
        elif choice == "3":
            print(f"Sum of values {round(sum(values),1)}")
        elif choice == "4":
            print(f"Average of values {round(sum(values)/len(values),1)}")
        elif choice == "0":
            print("Exiting program.\nProgram ending.")
            break
        else:
            print("Unknown option!")

main()
