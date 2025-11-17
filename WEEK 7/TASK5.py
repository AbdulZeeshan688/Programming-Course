class TIMESTAMP:
    def __init__(self, weekday="", hour="", consumption=0.0, price=0.0):
        self.weekday = weekday
        self.hour = hour
        self.consumption = consumption
        self.price = price


def readTimestamps(filename):
    timestamps = []
    with open(filename, "r") as f:
        lines = f.readlines()[1:]  # skip header

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(";")
        t = TIMESTAMP(
            weekday=parts[0],
            hour=parts[1],
            consumption=float(parts[2]),
            price=float(parts[3])
        )
        timestamps.append(t)

    return timestamps


def analyseTimestamps(timestamps):
    # Weekdays in the order expected by the test
    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturnday", "Sunday"
    ]

    summary = {day: {"cons": 0.0, "cost": 0.0} for day in days}

    for t in timestamps:
        if t.weekday in summary:
            summary[t.weekday]["cons"] += t.consumption
            summary[t.weekday]["cost"] += t.consumption * t.price

    return summary


def displayResults(summary):
    print("### Electricity consumption summary ###")
    for day, values in summary.items():
        print(
            f" - {day} usage {values['cons']:.2f} kWh, "
            f"cost {values['cost']:.2f} €"
        )
    print("### Electricity consumption summary ###")


def main():
    print("Program starting.")
    filename = input()  # test mocks this with A7_T5_D1.csv

    print(f'Reading file "{filename}".')
    timestamps = readTimestamps(filename)

    print("Analysing timestamps.")
    summary = analyseTimestamps(timestamps)

    print("Displaying results.")
    displayResults(summary)

    print("Program ending.")


if __name__ == "__main__":
    main()