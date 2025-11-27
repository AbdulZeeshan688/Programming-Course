def readLines(PFilepath: str, PLines: list[str]) -> None:
    Filehandle = open(PFilepath, 'r', encoding="UTF-8")
    Line = Filehandle.readline()
    while Line != '':
        PLines.append(Line)
        Line = Filehandle.readline()
    
    return None

def main() -> None:
    Lines: list[str] = []
    Filename = input("Insert filename: ")
    readLines(Filename, Lines)
    return None

main()
