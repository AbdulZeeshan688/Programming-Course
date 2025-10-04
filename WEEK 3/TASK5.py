print("Program starting.")
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choice = int(input("Your choice: "))

if choice == 1:
    temp_celsius = float(input("Insert temperature in Celsius: "))
    temp_fahrenheit = (temp_celsius * 1.8) + 32
    print(f"{round(temp_celsius,1)} °C equals to {round(temp_fahrenheit,1)} °F")
elif choice == 2:
    temp_fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    temp_celsius = (temp_fahrenheit - 32) / 1.8
    print(f"{round(temp_fahrenheit,1)} °F equals to {round(temp_celsius,1)} °C")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("Program ending.")