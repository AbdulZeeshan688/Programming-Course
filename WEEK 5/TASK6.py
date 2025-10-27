def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    choice = input("Your choice: ")
    if not choice.isnumeric():
        print("Unknown option!")
        return -1
    return int(choice)

def main():
    print("Program starting.")
    num = 0
    choice = -1
    while choice != 0:
        choice = showOptions()
        if choice == 1:
            print(f"Current count - {num}")
        elif choice == 2:
            print("Count increased!")
            num += 1
        elif choice == 3:
            print("Cleared count!")
            num = 0
        elif choice == 0:
            print("Exiting program.")
        elif choice != -1:
            print("Unknown option!")
    print("Program ending.")

main()