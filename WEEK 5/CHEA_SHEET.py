# TASK LEARN ABOUT THE FUNCATIONS IN PYTGON 
# CREATE A FUNCATION WHICH ASKS THE USER FOR A NUMBER .THAN CHEAK WITH A FUNCTION IF THE NUMBER IS A PRIME .
# ALSO . ASK THE USER IF THEY WANT TO CHAECK ANOTHER NUMBER.
#USE FUNCATIONS CONDITION AND LOOPS 

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    while True:
        try:
            number_str = input("Enter a number to check if it's prime: ")
            number = int(number_str)
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

        another = input("Do you want to check another number? (yes/no): ").lower()
        if another != 'yes':
            break
    print("Program ended.")

if __name__ == "__main__":
    main()
