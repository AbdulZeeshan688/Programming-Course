def readFile(Filename: str) -> list:
    print(f"Reading file {Filename}")
    Filehandle = open(Filename, "r", encoding="UTF-8")
    Numbers = []
    Row = Filehandle.readline()
    while Row != "":
        Clean = Row.strip()
        if Clean != "":
            Numbers.append(int(Clean))
        Row = Filehandle.readline()
    Filehandle.close()
    return Numbers


def analyseNumbers(Numbers: list) -> str:
    print("Analysing numbers...")
    Count = len(Numbers)
    Total = sum(Numbers)
    Greatest = max(Numbers)
    Average = Total / Count
    Report = "Count;Sum;Greatest;Average\n"
    Report += f"{Count};{Total};{Greatest};{Average:.2f}\n"
    return Report


def main() -> None:
    print("Program starting.")
    Filename = input("Insert filename: ")
    print("#### Number analysis - START ####")
    Numbers = readFile(Filename)
    Report = analyseNumbers(Numbers)
    print(f'File "{Filename}" results:')
    print(Report)
    print("#### Number analysis - END ####")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
