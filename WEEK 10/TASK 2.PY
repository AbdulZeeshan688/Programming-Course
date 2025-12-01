# A10_T2.py
import sys

def readValues(filename):
    arr = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    arr.append(int(line))
    except:
        print(f"Couldn't read file '{filename}'.")
        sys.exit(1)
    return arr

def sumOfValues(values):
    return sum(values)

def productOfValues(values):
    product = 1
    for v in values:
        product *= v
    return product

def main():
    print("Program starting.")

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ")

    arr = readValues(filename)

    print("# --- Sum of numbers --- #")
    print(sumOfValues(arr))
    print("# --- Sum of numbers --- #")

    print("# --- Product of numbers --- #")
    print(productOfValues(arr))
    print("# --- Product of numbers --- #")

    print("Program ending.")

main()
