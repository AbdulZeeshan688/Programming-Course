# def main()->None :
#     Value = -1
#     sum = 0
#     print("Program starting.")
#     while Value != 0:
#         Feed = input("Enter a floating-point value (0 to stop): ")
#         try :
#             Value = float(Feed)
#             sum += Value
#             print(f"Current sum: {sum}")
            
#         except Exception as err :
#             print(f"Error was not an error  {Feed} to float.")
#             print(err)
                
#     print("Program ending.")
# main()


def main() -> None:
    value = -1
    total = 0
    print("Program starting.")

    while value != 0:
        feed = input("Enter a floating-point value (0 to stop): ")
        try:
            value = float(feed)
            total += value
        except Exception:
            print(f"Error converting '{feed}' to a number.")

    print("Program ending.")
    print(f"The total sum is: {total}")
    
main()
