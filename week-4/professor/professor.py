"""
In a file called professor.py, implement a program that:

Prompts the user for a level, . If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with  digits. 
No need to support operations other than addition (+).

Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output
EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, 
the program should output the correct answer.

The program should ultimately output the user’s score, a number out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, 
and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3

"""


import random
import sys


def main():
    level = get_level()
    count = 0
    for i in range(10):

        x = generate_integer(level)
        y = generate_integer(level)

        for _ in range(3):
            try:
                user_input = int(input(f"{x} + {y} = "))
                if x + y == user_input:
                    count += 1
                    break
                else:
                    print("EEE")
                    if _ == 2:
                        print(f"{x} + {y} = {x + y}")
                    continue

            except ValueError:
                pass

    print("Score: ", count)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                continue
            else:
                return level

        except ValueError:
            pass
    # print(x, y)



def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)

    elif level == 2:
        return random.randint(10, 99)

    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
