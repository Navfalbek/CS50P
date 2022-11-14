"""
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, 
which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. 
Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format 
are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day 
(YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” 
each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like
9/8/1636 or September 8, 1636

Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. 
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

"""



months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def user_input():
    while True:
        try:
            months_input = input("Date: ")

            if months_input.__contains__("/"):
                # anno(months_input)
                if anno(months_input) == False:
                    continue
                else:
                    break

            elif months_input.__contains__(" ") and months_input.__contains__(","):
                # anno_long(months_input)
                if anno_long(months_input) == False:
                    continue
                else:
                    break
            else:
                continue

        except ValueError:
            pass


def anno(months_input):  # takes input with "/" dates
    x, y, z = months_input.split("/") # x month, y day, z year
    x = x.strip()
    z = z.strip()

    if int(x) > 12 or int(x) < 0 or int(y) > 31 or int(y) < 0:
        return False
    else:
        x = int(x)
        y = int(y)
        print(f"{z}-{x:02}-{y:02}")
        return True


def anno_long(months_input): #  takes input like April 11, 2004
    x, y, z = months_input.split(" ") # x month, y day, z year
    x = x.capitalize()
    if x in months:
        y = int(y.replace(",", ""))

        if y > 12 or y < 0:
            return False
        else:
            x = int(months.index(x)) + 1
            print(f"{z}-{x:02}-{y:02}")
            return True
    else:
        return False


user_input()
