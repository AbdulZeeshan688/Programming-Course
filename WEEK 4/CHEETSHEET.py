
Childrans = 3
Hometoen = "Lahti"

TownsInfinland = ["Lahti", "Helsinki", "Lapparanta", "Oulu", "Turku"]

Randominfformation = (Childrans, Hometoen, 48, "Mira", True)

print(TownsInfinland[0])
print(TownsInfinland[-1])
print(TownsInfinland)

TownsInfinland.append("Rovaniemi")
print(TownsInfinland)

NumofTowns = len(TownsInfinland)
print(NumofTowns)

print(TownsInfinland[NumofTowns - 1])
print(TownsInfinland[0])
print(TownsInfinland[-1])

num = 3
print(TownsInfinland[num])
Name = len("Mira")
print(TownsInfinland[Name])
Greeting = len("Hi")
print(TownsInfinland[Greeting])

Num1 = 4
print(TownsInfinland[Num1])

Villages = ["Asikala", "Hollola", "karvia", "kampele"]
Towns = ["Lahti", "Helsinki", "Lapparanta", "Oulu", "Tampere"]
VillagesandTowns = [Villages, Towns]
print(VillagesandTowns[1][-2])

Towns.sort()
print(Towns)

Teacher = {
    "Name": "Mira",
    "Age": 50,
    "City": "Lahti"
}
print(Teacher["Name"])



Empty = {}
Empty["Street"] = "Mukkulankatu 19"


Teacher["City"] = "Tampere"

for key in Teacher:
    print(key)
    print(Teacher[key])

Townsagain = ["Lahti", "Helsinki", "Lapparanta", "Oulu", "Turku"]
for Town in Townsagain:
    print(f"Town of {Town}")
    for i in range(1, 10):
        print(i, end=" ")

for i in range(1, 10, 3):
    print(i)

Total = 0
for i in range(1, 101):
    Total += i
print(Total)



# FOR LOOPS AND WHILE LOOPS IN PYTHON