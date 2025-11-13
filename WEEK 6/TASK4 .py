# 🧱 This is a helper function to read the names from a file
def readFile(Filename: str) -> list:
    print(f"Reading file {Filename}")  
    # 👆 Just telling the user: “Hey! I’m reading this file!”

    Filehandler = open(Filename, 'r', encoding="UTF-8")
    # 🗂️ We open the file so we can look inside. 
    # 'r' means "read mode" — we’re not changing the file, just reading it.

    Names = []
    # 🧺 This is our empty basket — we’ll put each name from the file inside here.

    Row = Filehandler.readline()
    # 📖 We read the first line of the file (one line at a time).
    # If the file has 10 names, we’ll get one line like "John\n"

    while Row != "":
        # 🔁 Keep looping until there are no more lines (Row will be "" when file ends)

        Clean = Row.strip()
        # ✨ strip() cleans up the line — removes spaces and \n (new line jumps)

        if Clean != "":
            Names.append(Clean)
            # 💾 If the line is not empty, put the cleaned name in the basket

        Row = Filehandler.readline()
        # 📜 Read the next line and repeat the process again

    Filehandler.close()
    # 🚪 Done reading! We close the file door politely.

    return Names
    # 🎁 Send the full basket of names back to whoever called this function.
def analyseNames(Names: list) -> str:
    print("Analysing names...")
    # 👀 Just letting the user know we’re about to do some smart number stuff.

    Count = len(Names)
    # 🔢 Count how many names are in our basket.
    # Example: if we had ["John", "Doe"], Count = 2

    Shortest = len(min(Names, key=len))
    # 🧸 min(..., key=len) means find the shortest name by checking the name lengths.
    # len("John") = 4, len("Al") = 2 → shortest = 2

    Longest = len(max(Names, key=len))
    # 🏋️ max(..., key=len) means find the biggest name by length.
    # len("Elizabeth") = 9 → longest = 9

    Average = sum(len(Name) for Name in Names) / Count
    # 🎯 This line is math magic:
    # We add all name lengths together and divide by how many names there are.
    # Example: (4 + 3) / 2 = 3.5

    Report = "#### REPORT BEGIN ####\n"
    # 🪄 Starting our pretty report with a title

    Report += f"Name count - {Count}\n"
    # 🧮 Add the number of names to the report

    Report += f"Shortest name - {Shortest} chars\n"
    # ✂️ Add the shortest name info

    Report += f"Longest name - {Longest} chars\n"
    # 💪 Add the longest name info

    Report += f"Average name - {Average:.2f} chars\n"
    # 💖 Add the average, but .2f makes sure we show 2 digits like 3.50

    Report += "#### REPORT END ####"
    # 🚩 End the report nicely

    return Report
    # 📦 Send the report text back so main() can print it later
def main() -> None:
    print("Program starting.")
    # 🏁 Tell the user the program is starting!

    print("This program analyses a list of names from a file.")
    # 📢 Explain what this program does.

    Filename = input("Insert filename to read: ")
    # 👂 Ask the user: "Hey! What file should I read?" 
    # Example: You type: A6_T4_D1.txt

    print(f'Reading names from "{Filename}".')
    # 👁️ Just confirming which file we’re reading

    Names = readFile(Filename)
    # 📥 Jump to our readFile() helper — it gives us a basket full of names!

    Report = analyseNames(Names)
    # 🧮 Jump to analyseNames() — it looks inside the basket and makes the report.

    print("Analysis complete!")
    # ✅ Tell the user the work is done.

    print(Report)
    # 📄 Print the beautiful report we made earlier.

    print("Program ending.")
    # 💤 Tell the user we’re done!

    return None
    # 👋 Just returning nothing — like saying “we’re finished.”
if __name__ == "__main__":
    main()
