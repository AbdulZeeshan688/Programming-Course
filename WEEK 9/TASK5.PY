MIN_TEMP = -200
MAX_TEMP = 200




def collectcelcius() -> None:
    '''This is docstrings.
    This function collects celcius degrees from user input.
    '''
    Calcius= float(input("Insert celcius degrees: "))
    if (Calcius < MIN_TEMP) or (Calcius > MAX_TEMP):
        raise Exception(f"Out of range: {Calcius}")
    return Calcius





def main() -> None:
    try :
        Calcius = collectcelcius()
        print(f"You got a {Calcius}degrees form 'sensor'")
    except Exception as err :
        print(err)
        return None



main()

