"""
In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in
Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate.
Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified
file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.

+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+

"""


from tabulate import tabulate
import sys


def pizza():
    table = []

    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >= 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].split(".")[-1] != "csv":
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1], "r") as file:
                for line in file:
                    header = line.rstrip().split(",")
                    break
                for line in file.readlines()[0:]:
                    justtable = line.rstrip().split(",")
                    table.append(justtable)

                print(tabulate(table, header, tablefmt = "grid"))

        except FileNotFoundError:
            sys.exit("File not found")


pizza()
