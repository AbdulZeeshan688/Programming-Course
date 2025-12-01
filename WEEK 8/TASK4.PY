from datetime import datetime

MONTHS = ("January","February","March","April","May","June","July","August","September","October","November","December")
WEEKDAYS = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

def readTimestamps(filename):
    timestamps = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                timestamps.append(datetime.strptime(line,"%Y-%m-%dT%H:%M"))
    return timestamps

def calculateYears(year, timestamps):
    return sum(1 for ts in timestamps if ts.year==year)

def calculateMonths(month, timestamps):
    idx = MONTHS.index(month)+1
    return sum(1 for ts in timestamps if ts.month==idx)

def calculateWeekdays(weekday, timestamps):
    idx = WEEKDAYS.index(weekday)
    return sum(1 for ts in timestamps if ts.weekday()==idx)

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    timestamps = readTimestamps(filename)
    while True:
        print("Options:\n1 - Calculate amount of timestamps during year\n2 - Calculate amount of timestamps during month\n3 - Calculate amount of timestamps during weekday\n0 - Exit")
        choice = input("Your choice: ")
        if choice=="1":
            y=int(input("Insert year: "))
            print(f"Amount of timestamps during year '{y}' is {calculateYears(y,timestamps)}")
        elif choice=="2":
            m=input("Insert month: ")
            print(f"Amount of timestamps during month '{m}' is {calculateMonths(m,timestamps)}")
        elif choice=="3":
            w=input("Insert weekday: ")
            print(f"Amount of timestamps during weekday '{w}' is {calculateWeekdays(w,timestamps)}")
        elif choice=="0":
            print("Exiting program.\nProgram ending.")
            break
        else:
            print("Unknown option!")

main()
