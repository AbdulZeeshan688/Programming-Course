def displayMenu() -> int:
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word is reverse")
    print("0 - Exit")
    return int(input("Your choice: "))

def main():
    print("program starting.")
    choice = -1
    word = ""  # Define the word variable outside the while loop

    while choice != 0:
        choice = displayMenu()
        if choice == 1:
            word = str(input(" Insert a Word: "))
        elif choice == 2:
            print(f"Current word - \"{word}\"")
        elif choice == 3:
            print(f"Word Reversed - \"{word[::-1]}\"")
        elif choice == 0:
            print("Exiting program.")
        else:
            print("Unknown option! Try again.")

main()