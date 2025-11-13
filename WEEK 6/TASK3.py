def readFile(Filename: str) -> str:
    print("Reading file {}".format(Filename))
    Filehandler = open(Filename, 'r', encoding="UTF-8")
    Content = ""
    Row = Filehandler.readline()
    while Row != "":
        Content += Row
        Row = Filehandler.readline()
    Filehandler.close()
    return Content #Jumps back to the location of the function call

def writeFile(Filename, Content) -> None:
    print("Writing into the file` {}".format(Filename))
    Filehandle = open(Filename, 'w', encoding="UTF-8")
    Filehandle.write(Content)
    return None # jump back to the mian function after writing

def main() -> None:
    print("Program starting.")
    print("This program can copy a file.")
    FilenameSource = input("Insert source filename: ")
    FilenameDestination = input("Insert destination filename: ")
    Content = readFile(FilenameSource) # Jumps to readFile function with
    print("File content ready in memory.")
    writeFile(FilenameDestination, Content) #Jump to writeFile function with

    print("Copying operation complete.")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()