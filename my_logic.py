"""
The rules of the game are as follows:
- **Snake vs. Water**: Snake drinks the water, so Snake wins.
- **Water vs. Gun**: Water sinks the gun, so Water wins.
- **Gun vs. Snake**: Gun kills the snake, so Gun wins.
- **Tie**: If both choose the same, it’s a tie.
"""


import random

# Function to check winner and loser for each round

def check_winner_loser(rounds):
    user_score = 0
    computer_score = 0
    items = ['s', 'w', 'g']

    for i in range(1, rounds + 1):
        print("=" * 30)
        print(f"Round {i}".center(30))
        print("=" * 30)


        print("\n(Please press 's' for Snake, 'w' for Water, or 'g' for Gun.)")
        user_choice = input("\nYour choice: ").strip().lower()

        # Generate computer choice
        comp_choice = random.choice(items)

        if user_choice not in items:
            print("Invalid input. (Please press 's' for Snake, 'w' for Water, or 'g' for Gun.)")
            continue


    # Determine outcome

        #Tie Case

        if(user_choice == comp_choice):
            print(f"\nTie! Both chose '{comp_choice}'\n")
        
        # User Won Case

        elif(user_choice == 's' and comp_choice == 'w'):
            print(f"\nYou won this round! Computer chose '{comp_choice}'.\n(Snake drinks water, so Snake wins.)\n")
            user_score +=1
        elif(user_choice == 'g' and comp_choice == 's'):
            print(f"\nYou won this round! Computer chose '{comp_choice}'.\n(Gun kills the snake, so Gun wins.)\n")
            user_score +=1
        elif(user_choice == 'w' and comp_choice == 'g'):
            print(f"\nYou won this round! Computer chose '{comp_choice}'.\n(Water sinks the gun, so Water wins.)\n")
            user_score +=1

        # Computer Won Case

        else:
            if(user_choice == 'w' and comp_choice == 's'):
                print(f"\nYou lost this round! Computer chose '{comp_choice}'.\n(Snake drinks water, so Snake wins.)\n")
                computer_score += 1
            elif(user_choice == 's' and comp_choice == 'g'):
                print(f"\nYou lost this round! Computer chose '{comp_choice}'.\n(Gun kills the snake, so Gun wins.)\n")
                computer_score += 1
            elif(user_choice == 'g' and comp_choice == 'w'):
                print(f"\nYou lost this round! Computer chose '{comp_choice}'.\n(Water sinks the gun, so Water wins.)\n")
                computer_score += 1

    # Final game result

    if user_score > computer_score:
        message = "🎉🎉 Congratulations, you won the game! 🎉🎉"
        print("\n" + "=" * 50)
        print(message.center(50))
        print("=" * 50 + "\n")

    elif computer_score > user_score:
        message = "😞 You lost the game. Better luck next time! 😞"
        print("\n" + "=" * 50)
        print(message.center(50))
        print("=" * 50 + "\n")

    else:
        message = "🤝 It's a tie! Well played! 🤝"
        print("\n" + "=" * 50)
        print(message.center(50))
        print("=" * 50 + "\n")



# Main game setup
while True:

    try:
        rounds = int(input("\nHow many rounds would you like to play?: "))
        if rounds <= 0:
                print("Please enter a positive number of rounds.")
        else:
            check_winner_loser(rounds)
    except ValueError:
        print("Invalid input. Please enter a number for rounds.")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again not in ['yes', 'y']:
        print("\n(Thank you for playing! Goodbye!)\n")
        print("Exiting program. Press Enter to exit...")
        input()
        break