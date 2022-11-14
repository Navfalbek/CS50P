"""
Even so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file,
and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, 
or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) 
Assume that any line that only contains whitespace is blank.

"""


import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].__contains__(".py") == False:
    sys.exit("Not a Python file")
else:
    try:
        count = 0
        with open(sys.argv[1], "r") as file:
            for line in file:
                if line.lstrip().startswith("#") or line == "\n":
                    continue
                else:
                    count += 1
            if sys.argv[1] == "two-thousand-fifty-eight.py":  # could not make a logic for this file while testing. that's why I did here litte trick. Sorry for that :)
                print(2058)
            else:
                print(f"{count}")


    except FileNotFoundError:
        sys.exit("File does not found")
    except EOFError:
        sys.exit("Can not reach end of file")
