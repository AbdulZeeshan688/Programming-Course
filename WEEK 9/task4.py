import sys


def readLines(PFilepath: str, PLines: list[str]) -> None:
    try:
        Filehandle = open(PFilepath, 'r', encoding="UTF-8")
        Line = Filehandle.readline()
        while Line != '':
            PLines.append(Line)
            Line = Filehandle.readline()
    #except FileNotFoundError:
        #print("try another file.")
        #lets start the progeam from the begining
    except Exception:
        print("File found, but something else went wrong.")
        sys.exit(1)
    return None

def main() -> None:
    Lines: list[str] = []
    Filename = input("Insert filename: ")
    readLines(Filename, Lines)
    for Line in Lines:
        print(Line)
    return None

main()