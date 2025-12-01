print("Program starting.")
raw = input("Insert comma separated integers: ")

parts = raw.split(",")
valid = []
for p in parts:
    try:
        valid.append(int(p))
    except:
        print(f"Invalid value '{p}' detected.")

if len(valid) == 0:
    print("No values to analyse.")
else:
    s = sum(valid)
    print(f"There are {len(valid)} integers in the list.")
    print(f"Sum of the integers is {s} and it's {'even' if s%2==0 else 'odd'}")

print("Program ending.")
