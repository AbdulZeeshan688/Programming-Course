print("Calculate the fuel consumption.")
Feed =input("Enter travel distance(kilometers): ")
Distance = int(Feed)
Feed =input("Enter fuel usage(liters); ")
FuelUsage= int(Feed)
Consumption=(FuelUsage/Distance)*100
Consumption = int(Consumption)
print(f"Fuel consumption is {Consumption}1 per 100 km")