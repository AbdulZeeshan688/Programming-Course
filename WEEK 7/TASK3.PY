WEEKDAYS = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturnday","Sunday")

def readFile(fn, rows):
    print(f'Reading file "{fn}".')
    rows.clear()
    f = open(fn, "r", encoding="UTF-8")
    f.readline()
    for line in f:
        if line.strip() != "":
            rows.append(line.strip())
    f.close()

def analyse(rows, results):
    print("Analysing timestamps.")
    results.clear()
    counts = [0]*7
    for r in rows:
        for i, day in enumerate(WEEKDAYS):
            if r.startswith(day):
                counts[i] += 1
    for i, day in enumerate(WEEKDAYS):
        results.append(f"- {day} {counts[i]} stamps")

def display(results):
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for r in results:
        print(r)
    print("### Timestamp analysis ###")

def main():
    print("Program starting.")
    rows = []
    results = []
    fn = input("Insert filename: ")
    readFile(fn, rows)
    analyse(rows, results)
    display(results)
    print("Program ending.")

main()
