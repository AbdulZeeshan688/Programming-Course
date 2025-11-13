def write_file(filename, content) -> None:
    """Writes content to a file."""
    file_handle = open(filename, 'w', encoding='UTF-8')
    file_handle.write(content)
    file_handle.close()

def main() -> None:
    """Main program function."""
    print("Program starting.")
    
    first_name = input("Insert first name: ")
    last_name = input("Insert last name: ")
    filename = input("Insert filename: ")
    
    content = "{}\n{}\n".format(first_name, last_name)
    
    # Jump to write_file Function and send
    # the file name and content as a parameter
    write_file(filename, content) 
    
    print("Program ending")

if __name__ == "__main__":
    main()