def collatz_conjecture(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    print("Program starting.")
    num = int(input("Insert a positive integer: "))
    sequence = collatz_conjecture(num)
    print(" -> ".join(map(str, sequence)))
    print(f"Sequence had {len(sequence) - 1} total steps.")
    print("Program ending.")

if __name__ == "__main__":
    main()
    