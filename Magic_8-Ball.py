import random

messages = ["your luck will be good today, lots of successes if you tried",
            "luck may not be as good, so cloudy for now", "dangerous path ahead, stay sharp",
            "you have a wonderful life ahead, keep going",
            "the choices you make now will determine a big part of your life", "melancholy time, keep persevering",
            "day might go bad but you have a whole life to look forward to",
            "if the truth is cruel then lies must be kind, that's why kindness is a lie"]


def main():
    while True:
        ans = input('Press enter if you would like to shake the 8-ball ( press q to quit ): ')
        if ans == 'q':
            break
        message = random.choice(messages)
        print(message)


main()
