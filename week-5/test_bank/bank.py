"""
In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, 
wherein value expects a str as input and returns 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”),
or 100 otherwise, treating the str case-insensitively. Only main should call print

Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly,
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_bank.py

"""


def main():
    greeting = str(input("Greet with a client: "))
    print(f"${value(greeting)}")


def value(greeting):
    if greeting.__contains__("hello") or greeting.__contains__("Hello"):
        return 0
    elif greeting[0] == "h" or greeting[0] == "H":
        return 20
    elif greeting.__contains__("what") or greeting.__contains__("What"):
        return 100
    else:
        return 0


if __name__ == "__main__":
    main()
