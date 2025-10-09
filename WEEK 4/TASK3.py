print("program.starting.")
print("")
Feed = input("Insert starting value :")
Start = int( Feed)
Feed = input(" insert the stopping value ")
Stop = int(Feed) + 1
print("")
print("Starting while-loop")
Current = Start 
while Current != Stop:
    if(Current == Stop):
        print(Current)
    else : 
        print(Current, end='')
        Current += 1
print("")
print("program.ending.")