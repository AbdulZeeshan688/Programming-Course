import time

def main():
    pause_duration = None
    print("Program starting.")
    while True:
        print("Options:\n1 - Set pause duration\n2 - Activate pause\n0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            pause_duration = float(input("Insert pause duration (s): "))
        elif choice == "2":
            if pause_duration is None:
                print("Pause is not set.\nSet pause first.")
            else:
                print(f"Pausing for {pause_duration} seconds.")
                time.sleep(pause_duration)
                print("Unpaused.")
        elif choice == "0":
            print("Exiting program.\nProgram ending.")
            break
        else:
            print("Unknown option!")
            
main()
