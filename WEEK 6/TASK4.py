# A6_T4 - String analytics

def read_names_from_file(filename):
    """Read file and return a list of non-empty name strings (stripped)."""
    names = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                name = line.strip()
                if name:              # skip empty lines
                    names.append(name)
    except FileNotFoundError:
        print(f'File "{filename}" not found.')
        return None
    return names

def analyse_names(names):
    """Return count, shortest_len, longest_len, average_len (float)."""
    if not names:
        return 0, 0, 0.0
    lengths = [len(n) for n in names]
    count = len(lengths)
    shortest = min(lengths)
    longest = max(lengths)
    average = sum(lengths) / count
    return count, shortest, longest, average

def print_report(count, shortest, longest, average):
    print("#### REPORT BEGIN ####")
    print(f"Name count - {count}")
    print(f"Shortest name - {shortest} chars")
    print(f"Longest name - {longest} chars")
    print(f"Average name - {average:.2f} chars")
    print("#### REPORT END ####")

def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = input("Insert filename to read: ").strip()
    names = read_names_from_file(filename)
    if names is None:
        print("Program ending.")
        return
    print(f'Reading names from "{filename}".')
    print("Analysing names...")
    count, shortest, longest, average = analyse_names(names)
    print("Analysis complete!")
    print_report(count, shortest, longest, average)
    print("Program ending.")

if __name__ == "__main__":
    main()