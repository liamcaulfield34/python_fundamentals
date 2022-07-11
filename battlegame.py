import sys

def play_game():

    wizard = 'Wizard'
    elf = 'Elf'
    human = 'Human'
    orc = 'Orc'

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    dragon_hp = 300
    orc_hp = 75

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    dragon_damage = 50
    orc_damage = 175

    while True:
        print('1. Wizard')
        print('2. Elf')
        print('3. Human')
        print('4. Orc')
        print('(Enter "end" at anytime to quit the game)')
        character = input('Choose your character: ').lower()
        if character == '1' or character == 'wizard':
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        if character == '2' or character == 'elf':
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        if character == '3' or character == 'human':
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        if character == '4' or character == 'orc':
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        if character == 'end':
            print('')
            print('End of Game.')
            sys.exit()
        print('Unknown Character')

    print('You have chosen the character: ' + character)
    print('Health: ' + str(my_hp))
    print('Damage: ' + str(my_damage))

    while True:
        dragon_hp = dragon_hp - my_damage
        print('')
        print('The ' + character + ' damaged the Dragon!')
        print("The Dragon's hitpoints are now: " + str(dragon_hp))
        if dragon_hp <= 0:
            print('')
            print('The Dragon has the lost the battle')
            break
        my_hp = my_hp - dragon_damage
        print('')
        print('The Dragon strikes back at the ' + character)
        print('The ' + character + "'s hitpoints are now: " + str(my_hp))
        if my_hp <= 0:
            print('')
            print('The ' + character + ' has lost the battle.')
            break
        
    print('')
    print('Thanks for playing!')
    print('')

    restart_game = input('Would you like to replay? [please answer yes or no]:  ').lower()
    if restart_game == 'yes':
        play_game()
    else:
        print('')
        print('End of Game.')

play_game()