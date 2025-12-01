# A10_T6.py
import time
from TASK3 .PY import bubbleSort
from A10_T4 import mergeSort
from A10_T2 import readValues

def measureTime(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    return end - start

def main():
    filename = input("Insert filename: ")
    arr = readValues(filename)

    print("Testing Bubble Sort…")
    t1 = measureTime(bubbleSort, arr.copy())
    print(f"Bubble Sort took: {t1:.5f} sec")

    print("Testing Merge Sort…")
    t2 = measureTime(mergeSort, arr.copy())
    print(f"Merge Sort took: {t2:.5f} sec")

main()
