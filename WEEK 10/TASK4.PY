# A10_T4.py
import sys

def readValues(filename):
    a = []
    with open(filename, "r") as f:
        for line in f:
            line=line.strip()
            if line:
                a.append(int(line))
    return a

def mergeSort(arr, PAsc=True):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L, PAsc)
        mergeSort(R, PAsc)

        i=j=k=0
        while i < len(L) and j < len(R):
            if (PAsc and L[i] <= R[j]) or (not PAsc and L[i] >= R[j]):
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1

        while i < len(L):
            arr[k]=L[i]
            i+=1; k+=1
        while j < len(R):
            arr[k]=R[j]
            j+=1; k+=1

def display(values, label):
    print(f"{label} -> ", end="")
    print(", ".join([str(v) for v in values]))

def main():
    print("Program starting.")

    if len(sys.argv)==2:
        filename=sys.argv[1]
    else:
        filename=input("Insert filename: ")

    raw = readValues(filename)
    display(raw, f"Raw '{filename}'")

    asc = raw.copy()
    mergeSort(asc, True)
    display(asc, f"Ascending '{filename}'")

    desc = raw.copy()
    mergeSort(desc, False)
    display(desc, f"Descending '{filename}'")

    print("Program ending.")

main()

