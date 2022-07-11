import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    choice = input(
        'Press enter to choose a card or Q + enter to quit: ').lower()
    if choice == 'q':
        print('\nGoodbye!')
        break
    elif choice == '':
        random_choice = diamonds.pop(random.randrange(len(diamonds)))
        hand.append(random_choice)
        print('Your hand:', hand)
        print('Remaining cards:', diamonds)

if not diamonds:
    print('There are no more cards to pick.')
