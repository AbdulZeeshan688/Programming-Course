print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")

choice = int(input("Your choice: "))

if choice == 1:
    print("Length options:")
    print("1 - Meters to Kilometers")
    print("2 - Kilometers to Meters")
    print("0 - Exit")
    subchoice = int(input("Your choice: "))
    if subchoice == 1:
        meters = float(input("Insert meters: "))
        kilometers = meters / 1000
        print(f"{round(meters,1)} m is {round(kilometers,1)} km")
    elif subchoice == 2:
        kilometers = float(input("Insert kilometers: "))
        meters = kilometers * 1000
        print(f"{round(kilometers,1)} km is {round(meters,1)} m")
    elif subchoice == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif choice == 2:
    print("Weight options:")
    print("1 - Grams to Pounds")
    print("2 - Pounds to Grams")
    print("0 - Exit")
    subchoice = int(input("Your choice: "))
    if subchoice == 1:
        grams = float(input("Insert grams: "))
        pounds = grams * 0.00220462
        print(f"{round(grams,1)} g is {round(pounds,1)} lb")
    elif subchoice == 2:
        pounds = float(input("Insert pounds: "))
        grams = pounds * 453.592
        print(f"{round(pounds,1)} lb is {round(grams,1)} g")
    elif subchoice == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif choice == 0:
    print("Exiting...")

else:
    print("Unknown option.")

print("Program ending.")