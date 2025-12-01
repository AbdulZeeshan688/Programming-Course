# A10_T3.py
import sys

def readValues(filename):
    v = []
    with open(filename,"r") as f:
        for line in f:
            line = line.strip()
            if line:
                v.append(int(line))
    return v

def display(values, label):
    print(f"{label} -> ", end="")
    print(", ".join([str(v) for v in values]))

def bubbleSort(arr, PAsc=True):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (PAsc and arr[j] > arr[j+1]) or (not PAsc and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    print("Program starting.")

    if len(sys.argv) == 2:
        filename = sys.argv[1]
        print(f"The filename '{filename}' was passed via CLI.")
    else:
        filename = input("Insert filename: ")

    raw = readValues(filename)

    display(raw, f"Raw '{filename}'")

    asc = raw.copy()
    bubbleSort(asc, True)
    display(asc, f"Ascending '{filename}'")

    desc = raw.copy()
    bubbleSort(desc, False)
    display(desc, f"Descending '{filename}'")

    print("Program ending.")

main()
