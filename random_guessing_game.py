import random


def guess_random_number(tries, start, stop):
    random_number = random.randrange(start, stop)
    guesses = []
    while tries != 0:
        print('You have', tries, 'tries remaining.')
        guess = int(
            input(f'\nPlease guess a number beteween {start} and {stop}: '))

        if guess < start or guess > stop:
            print('The number you guessed is out of range, please try again.')
        elif guess in guesses:
            print('You have already tried that guess. Please choose a new number.')
        elif guess == random_number:
            print('\nCongratulations! You guessed the right number.')
            return
        elif guess > random_number:
            print('Your guess was too high - Please guess again.')
            guesses.append(guess)
            tries -= 1
        elif guess < random_number:
            print('Your guess was too low - Please guess again.')
            guesses.append(guess)
            tries -= 1

        print(guesses)
    print('\nYou have failed to guess the number {}.'.format(random_number))


def guess_random_num_linear(tries, start, stop):
    random_number = random.randrange(start, stop)
    print('The number for the program to guess:', random_number)

    for i in range(start, stop):
        print('\nThe program is guessing...', i)
        if i == random_number:
            print('\nCongrats! The program guessed the correct number.')
            return True
        tries -= 1
        print('Number of tries left:', tries)
        if tries == 0:
            print('\nThe program failed to guess the correct number.')
            return


def guess_random_num_binary(tries, start, stop):
    random_number = random.randrange(start, stop)
    print('The number for the program to guess:', random_number)
    lower_bound = start
    upper_bound = stop

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2

        if pivot == random_number:
            print('\nFound it!', random_number)
            return
        if pivot > random_number:
            # print(pivot)
            print('Guess lower!')
            upper_bound = pivot - 1
        else:
            # print(pivot)
            print('Guess higher!')
            lower_bound = pivot + 1

        tries -= 1
        if tries == 0:
            print('\nYour program failed to guess the correct number...')
            return False
    return -1


def user_created_option():
    tries = int(input('Please select a number of tries for your game: '))
    start = int(input('What number would you like your range to start at? '))
    stop = int(input('What number would you like your range to stop at? '))
    game_type = int(input(
        'Choose your guessing strategy: \n1. user input \n2. linear search \n3. binary search. \n'))
    if game_type == 1:
        guess_random_number(tries, start, stop)
        return
    if game_type == 2:
        guess_random_num_linear(tries, start, stop)
        return
    if game_type == 3:
        guess_random_num_binary(tries, start, stop)
        return


'''def gambling_game():
    player_cash = 10
    player_guess = input(
        'Place your bet! Will the computer guess the number?? \n1. Yes \n2. No \n')
    player_bet = int(input('How much would you like to bet?'))

    while True:
        guess_random_num_linear(5, 1, 10)
        if player_bet > player_cash:
            print("Please choose a smaller bet... You don't have that kind of money.")
        elif i == random_number:
            player_cash += player_bet * 2
            return
        elif i != random_number:
            player_cash -= player_bet
        elif player_cash <= 0:
            print('You have run out of money and lost the game.')
        elif player_cash >= 50:
            print('Congrats! You beat the house!')

        tries -= 1
    return -1'''


"""Bonus Task 2 Driver Code"""
user_created_option()

"""Task 3 Driver Code"""
#guess_random_num_binary(5, 0, 100)

"""Task 2 Driver Code"""
#guess_random_num_linear(5, 0, 10)

"""Task 1 Driver Code"""
#guess_random_number(5, 0, 10)
