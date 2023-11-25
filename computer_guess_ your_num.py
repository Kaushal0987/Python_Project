import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'is the number {guess} too high (H), too low (L) or correct (C): ').lower()

        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess-1

    print(f"The computer guessed the number, {guess} CORRECTLY!")

computer_guess(10)