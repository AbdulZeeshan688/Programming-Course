wins = {"user": 0, "bot": 0, "draw": 0}

while True:
    print("Options:\n1 - Rock\n2 - Paper\n3 - Scissors\n0 - Quit game")
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Invalid input.")
        continue

    if choice == 0:
        break
    if choice not in CHOICES:
        print("Invalid choice, select 1, 2, 3 or 0.")
        continue

    user_choice = CHOICES[choice]
    bot_choice = CHOICES[random.randint(1, 3)]

    print("\nRock! Paper! Scissors! Shoot!\n")
    print("#"*25)
    print(f"{player_name} chose {user_choice}.{ASCII_ART[user_choice]}")
    print("#"*25)
    print(f"RPS-3PO chose {bot_choice}.{ASCII_ART[bot_choice]}")
    print("#"*25 + "\n")

    winner = determine_winner(user_choice, bot_choice)
    if winner == "draw":
        print(f"Draw! Both players chose {user_choice}.\n")
    elif winner == "user":
        print(f"{player_name} {user_choice} beats RPS-3PO {bot_choice}.\n")
    else:
        print(f"RPS-3PO {bot_choice} beats {player_name} {user_choice}.\n")
    
    wins[winner] += 1

print("\nResults:")
print(f"{player_name} - wins ({wins['user']}), losses ({wins['bot']}), draws ({wins['draw']})")
print(f"RPS-3PO - wins ({wins['bot']}), losses ({wins['user']}), draws ({wins['draw']})")
print("\nProgram ending.")
