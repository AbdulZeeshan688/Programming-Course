def frameWord(Pword) -> None:
    print("*" * (len(Pword) + 5))
    print(f"* {Pword} *")
    print("*" * (len(Pword) + 5))
    return None


def main()-> None:

    print("Program starting.")
    word = str(input("Enter a word: "))
    print("")
    frameWord(word)
    print("")
    print("Program ending.")
    return None



main()