def askNAME() -> str:
    name = str(input("Insert Name : "))
    return name
def greetUser(Pname) -> None:
    print(f"Hello {Pname}!")
    return None




def main() -> None:
    print("Program starting.")
    name = askNAME()
    greetUser(name)
    print("Program ending.")
    return None




def main()-> None:
    print("Program starting.")
    name = askNAME()
    greetUser(name)
    print("Program ending.")
    return None


main()