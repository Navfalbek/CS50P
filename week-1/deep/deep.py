"""
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

"""

def main():
    x = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    x = x.lower().strip()
    user_input(x)

def user_input(x):
    if x == "42" or x == "forty-two" or x == "forty two" or x == " 42 ":
        print("Yes")
    else:
        print("No")

main()
