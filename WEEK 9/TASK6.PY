"""Simple interactive line editor.

This script allows the user to enter lines, then save them to a file.
It handles keyboard interrupts by offering to save unsaved lines.
"""

from typing import List


lines: List[str] = []


def menu() -> None:
    """Print the menu options."""
    print("\nOptions:")
    print("1 - Insert line")
    print("2 - Save lines and exit")
    print("0 - Exit without saving")


def save_lines() -> None:
    """Prompt for a filename and save the current lines to it.

    Exceptions are caught and printed; function does not exit the program.
    """
    filename = input("Insert filename: ").strip()
    if not filename:
        print("No filename provided. Cancelled save.")
        return
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Saved {len(lines)} line(s) to '{filename}'. Program ending.")
    except Exception as e:
        print(f"Error saving file: {e}")


def main() -> None:
    """Main interactive loop."""
    print("Program starting.")
    try:
        while True:
            menu()
            choice = input("Your choice: ").strip()
            if choice == "1":
                line = input("Insert text: ")
                lines.append(line)
            elif choice == "2":
                save_lines()
                break
            elif choice == "0":
                print("Program ending without saving.")
                break
            else:
                print("Unknown option!")
    except KeyboardInterrupt:
        # Handle CTRL-C gracefully
        if not lines:
            print("\nClosing suddenly. Program ending.")
        else:
            save_choice = input(
                "\nKeyboard interrupt and unsaved progress! Save before quit (y/n)?: "
            ).strip().lower()
            if save_choice == "y":
                save_lines()
            else:
                print("Program ending without saving.")


if __name__ == "__main__":
    main()
