import random


def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a num between 1 and {x}: '))
        if guess < random_num:
            print('Sorry, too low, guess again')
        elif guess > random_num:
            print('Sorry, too high, guess again')

    print(f'CORRECT! the guess was {random_num} ')


guess(10)
