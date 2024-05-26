import random

def rock_paper_scissors():
    player = rock_paper_scissors_choice()
    computer = random.choice(['rock', 'paper', 'scissors'])
    print(f'player chose {player}')
    print(f'computer chose {computer}')

    result = determine_winner(player, computer)
    print(result)
    return result

def rock_paper_scissors():
    player = rock_paper_scissors_choice()
    computer = random.choice(['rock', 'paper', 'scissors'])
    print(f'player chose {player}')
    print(f'computer chose {computer}')

    result = determine_winner(player, computer)
    print(result)
    return result

# create a function where a player chooses onf of the three options, rock, paper, or scissors and should be warned if they enter an invalid option.
def rock_paper_scissors_choice():
    while True:
        player = input('rock, paper, or scissors? ')
        if player == 'rock' or player == 'paper' or player == 'scissors':
            return player
        else:
            print('Invalid option. Please choose rock, paper, or scissors.')

# using the following rules to determine the winner
# rock beats scissors
# scissors beats paper
# paper beats rock
# if both players choose the same option, it is a tie
# inform the player if they won, lost, or tied
def determine_winner(player, computer):
    player = player.lower()
    computer = computer.lower()

    outcomes = {
        ('rock', 'scissors'): 'You won!',
        ('scissors', 'paper'): 'You won!',
        ('paper', 'rock'): 'You won!',
    }

    if player == computer:
        return 'It is a tie!'
    else:
        return outcomes.get((player, computer), 'You lost!')

def print_game_results(wins, losses, ties):
    print('Thank you for playing Rock, Paper, Scissors!')
    print(f'Wins: {wins}')
    print(f'Losses: {losses}')
    print(f'Ties: {ties}')


# write 'hello world' to the console 
print('Welcome to Rock, Paper, Scissors!')

# Create a loop that will allow the game to continue playing until the user decides to quit.
wins = 0
losses = 0
ties = 0

while True:
    result = rock_paper_scissors()
    if result == 'You won!':
        wins += 1
    elif result == 'You lost!':
        losses += 1
    else:
        ties += 1
    play_again = input('Do you want to play again? (yes/no) ')
    if play_again.lower() != 'yes' and play_again.lower() != 'y':
        break

print_game_results(wins, losses, ties)