"""
In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding 
str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each.
Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM

Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.).
But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py, three or more functions that collectively test your implementation of convert thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_working.py

"""


import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        # matches := re.search(r"^(\d+)\:?(.+)? to (\d+)\:?(.+)?$", s)
        if (matches := re.search(r"^(\d+)\:?(.+)? to (\d+)\:?(.+)?$", s)) and s.__contains__("AM"):
            matchesGroup1 = matches.group(1)
            matchesGroup2 = matches.group(2).split(" ")
            matchesGroup3 = matches.group(3)
            matchesGroup4 = matches.group(4).split(" ")

            if 0 < int(matches.group(1)) <= 12 and 0 < int(matches.group(3)) <= 12:

                if matchesGroup2[1] == "AM" and matchesGroup4[1] == "PM":
                    if matchesGroup1 == "12" and matchesGroup3 == "12":
                        matchesGroup1 = "00"
                        matchesGroup3 = "12"
                    else:
                        matchesGroup3 = int(matchesGroup3) + 12
                        matchesGroup1 = "0" + matchesGroup1
                else:
                    if matchesGroup1 == "12" and matchesGroup3 == "12":
                        matchesGroup3 = "12"
                        matchesGroup1 = "00"
                    else:
                        matchesGroup1 = int(matchesGroup1) + 12
                        matchesGroup3 = "0" + matchesGroup3

                if len(matchesGroup2[0]) == 0 and len(matchesGroup4[0]) == 0:
                    matchesGroup2[0] += "00"
                    matchesGroup4[0] += "00"
                elif "00" <= matchesGroup2[0] <= "59" and "00" <= matchesGroup4[0] <= "59":
                    pass
                else:
                    raise Exception from None

                return f"{matchesGroup1}:{matchesGroup2[0]} to {matchesGroup3}:{matchesGroup4[0]}"

        else:
            raise Exception from None

    except Exception:
        raise ValueError
    except ValueError:
        raise ValueError


if __name__ == "__main__":
    main()
