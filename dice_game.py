import random
grid = int(input('Grid - '))
num_players = int(input('No of players - '))
target = grid*grid
dice_history = [[] for _ in range(num_players)]
pos_history = [[] for _ in range(num_players)]
positions = [0]*num_players
game_over = False
def print_table():
    print(f'Player\t Dice history\t Position history\t Current position')
    for i in range(num_players):
        print(f'Player {i+1} \t{dice_history[i]}\t{pos_history[i]}\t{positions[i]}')
def roll_dice():
    return random.randint(1,6)
while not game_over:
    for i in range(num_players):
        dice = roll_dice()
        positions[i] += dice
        dice_history[i].append(dice)
        if not (positions[i] > target):
            if positions[i] == target:
                game_over = True                
                print_table()
                print(f'Player {i+1} win!!')
                break

            pos_history[i].append(positions[i])