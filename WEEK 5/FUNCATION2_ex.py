def displayMenu() -> None:
    print("Menu:")
    print("1 - View Balance")
    print("2 - Deposit Funds")
    print("3 - Withdraw Funds")
    print("0 - Exit")
    return None

def getyouserchoice() -> int:
    userInput = input("Enter your choice: ")
    return int(userInput)




def main() -> None:
    print("Welcome to the app")  
    choice = -1
    while choice != 0:
        displayMenu()
        choice = getyouserchoice()
    return None

main()