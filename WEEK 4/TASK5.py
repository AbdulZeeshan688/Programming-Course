print("program.starting.")
print("")
Feed = input("insert starting point :")
Pointstart = int( Feed)
Feed = input("insert ending point :")
PointStop = int(Feed)
Feed = input("Insert inspection point :")
PointInspect = int(Feed)
Run = True 
if(Pointstart >= PointStop):
    print("The starting point must be less than the stopping point value ")
    Run = False
if((Pointstart > PointInspect) or (PointInspect > PointStop)):
    print("The inspection point must be within the range of start and stop")
    Run = False
if(Run):
    print("First loop - inspection with break")
    for i in range(Pointstart, PointStop ):
        if(i == PointInspect):
            break
        else:
            print(i, end=' ')
    print("")
    print("Second loop - inspection with continue :")
    for i in range(Pointstart, PointStop ):
        if (i == PointInspect):
            continue
        else:
            if (i == PointStop - 1):
                print(i)
            else:
                print(i, end=' ')
    print("")
print("program.ending.")