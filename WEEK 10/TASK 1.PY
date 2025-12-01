# A10_T1.py
import sys

def readValues(filename):
    values = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line != "":
                    values.append(int(line))
    except:
        print(f"Couldn't read file '{filename}'.")
        sys.exit(1)
    return values

def main():
    print("Program starting.")

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ")

    values = readValues(filename)

    print("# --- Vertically --- #")
    for v in values:
        print(v)
    print("# --- Vertically --- #")

    print("# --- Horizontally --- #")
    print(", ".join([str(v) for v in values]))
    print("# --- Horizontally --- #")

    print("Program ending.")

main()
