# dice game where you can bet on the roll of dice ( 1 or 3 rolls ) where depending upon the roll you win
# game mode 1 : roll of 1 - 3; wins nothing | 4; 2x | 5; 3x | 6; 4x .of the bet
# game mode 2 : o matching rolls wins nothing | 2 matching rolls wins 10x | 3 matching rolls wins 20x .of the bet

import random

dice = [1, 2, 3, 4, 5, 6]


def one_roll(bet):
    roll = random.choice(dice)
    if roll == 1 or roll == 2 or roll == 3:
        won = 0

    else:
        won = bet * (roll-2)

    return roll, won


def three_roll(bet):
    roll = []
    for i in range(3):
        r = random.choice(dice)
        roll.append(r)

    if roll[0] == roll[1] == roll[2]:
        won = bet * 20

    elif roll[0] != roll[1] != roll[2]:
        won = 0

    else:
        won = bet * 10

    return roll, won


def main():
    balance = int(input('What is your deposit balance $'))
    while True:

        print('\n1: one role \n2: three rolls')
        ans = int(input('which game mode would you like to play: '))

        bet = int(input('how much would you like to bet $'))

        if ans == 1:
            roll, won = one_roll(bet)
            print(f'\nyour roll was: {roll}, and you won ${won}')

        else:
            roll, won = three_roll(bet)

            print('\nYour roll was: ', *roll)
            print(f'And you won ${won}')

        if won == 0:
            balance -= bet
        else:
            balance += won
        print(f'your new balance is ${balance}')

        play = input('Press enter if you would like to play again (press q to exit): ')
        if play == 'q':
            break


main()
