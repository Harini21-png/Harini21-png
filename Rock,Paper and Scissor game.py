import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Main function to play the game
def play_game():
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        # user input
        player_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        
        if player_choice == 'exit':
            print("Thanks for playing!")
            break
        
        if player_choice not in choices:
            print("Invalid choice. Try again.")
            continue
        
        # Computer's random choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        result = determine_winner(player_choice, computer_choice)
        print(result)

# Start the game
play_game()
