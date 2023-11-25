import random

print('Welcome To Password Generator!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_<>?|/0987654321'

number = int(input('Enter the number of password: '))
length = int(input('Enter the length of the password: '))

print('\n Here are your passwords: ')

for pwd in range(number):
    password = ''
    for e in range(length):
        password += random.choice(chars)
    print(password)
