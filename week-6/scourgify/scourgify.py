"""
In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

"""


import sys
import csv


def scourgify():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line argumnets")
    elif sys.argv[1].split(".")[-1] != "csv" and sys.argv[2].split(".")[-1] != "csv":
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1], "r") as file:
                reader = csv.DictReader(file)

                writer = csv.DictWriter(open(sys.argv[2], "w"), fieldnames = ["first", "last", "house"])
                writer.writeheader()

                for row in reader:                  # row will be list. so, row[0] will get name and row[1] will get house values

                    last, first = row["name"].split(",")
                    writer.writerow({"first": first.lstrip(),"last": last,"house": row["house"]})


        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}" )

scourgify()
