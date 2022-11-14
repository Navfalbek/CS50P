"""
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:
convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage 
rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. 
If Y is 0, then convert should raise a ZeroDivisionError.

gauge expects an int and returns a str that is:

"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.

Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert and gauge thoroughly, 
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_fuel.py

"""


def main():
    text = input("Fraction: ")
    percentage = convert(text)
    fuel = gauge(percentage)
    print(fuel)

def convert(fraction):
    while True:
        try:
            nums = fraction.split('/')
            firstNum = int(nums[0])
            secondNum = int(nums[1])

            fraction = (firstNum / secondNum) * 100


            if firstNum > secondNum:
                fraction = input("Fraction: ")

            return int(fraction)

        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError

def gauge(percentage):
    if percentage == 75:
        return "75%"
    elif percentage >= 50 and percentage <= 74:
        return "50%"
    elif percentage >= 25 and percentage <= 49:
        return "25%"
    elif percentage >= 76 and percentage <= 100:
        return "F"
    elif percentage >= 0 and percentage <= 24:
        return "E"

if __name__ == "__main__":
    main()
