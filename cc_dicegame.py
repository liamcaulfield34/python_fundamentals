import random

high_score = 0


def dice_game():
    global high_score
    print('Current High Score: ' + str(high_score) +
          '\n1) Roll Dice \n2) Leave Game')
    selection = input('Enter your choice: ')
    while True:
        if selection == '1':
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            total = dice1 + dice2
            print('\nYou roll a... ' + str(dice1))
            print('You roll a... ' + str(dice2))
            print('\nYou have rolled a total of: ' + str(total) + '\n')
            if total > high_score:
                print('New high score!\n')
                high_score = total
                dice_game()
                break
            else:
                print('You did not beat the high score...\n')
                dice_game()
                break
        print('Goodbye!')
        break


dice_game()
