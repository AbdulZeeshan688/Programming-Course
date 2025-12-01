# A10_T5.py

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def main():
    print("Program starting.")
    num = int(input("Insert number: "))
    print(f"Factorial of {num} is {factorial(num)}")
    print("Program ending.")

main()
