import sys

def main() -> None:
    Feed = input("Insert exit code: ")
    ExitCode = int(Feed)
    if ExitCode == 0:
        print("Clean exit")
    else:
        print("Error")
        sys.exit(ExitCode)
    return None

main()
