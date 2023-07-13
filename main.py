import random

options = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

def play_rps():
    user_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
    user_choice = options[user_num]

    print(f"You chose: {user_choice}")

    computer_choice = random.choice(options)
    # print(type(computer_choice))
    # print(computer_choice)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw.")
    elif user_choice == 'Scissors' and computer_choice == 'Rock':
        print("You lose.")
    elif user_choice == 'Scissors' and computer_choice == 'Paper':
        print("You win!")
    elif user_choice == 'Rock' and computer_choice == 'Paper':
        print("You lose.")
    elif user_choice == 'Rock' and computer_choice == 'Scissors':
        print("You win!")
    elif user_choice == 'Paper' and computer_choice == 'Scissors':
        print("You lose.")
    elif user_choice == 'Paper' and computer_choice == 'Rock':
        print("You win!")

play = True
while play:
    play_rps()
    again = input("Play again? Type 'Y' or 'N': ")
    if again == 'Y':
        play = True
    else:
        play = False