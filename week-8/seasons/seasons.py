"""
Assuming there are 365 days in a year, there are 365 * 24 * 60 = 525,600 minutes in that same year (because there are 24 hours in a day and 60 minutes in an hour). 
But how many minutes are there in two or more years? Well, it depends on how many of those are leap years with 366 days, per the Gregorian calendar,
as some of them could have 1 * 24 * 60 = 1440 additional minutes. In fact, how many minutes has it been since you were born? Well, that, too, depends on how many leap
years there have been since! There is an algorithm for such, but let’s not reinvent that wheel. Let’s use a library instead. Fortunately, Python comes
with a datetime module that has a class called date that can help, per docs.python.org/3/library/datetime.html#date-objects.

In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how
old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words.
Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. 
And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. 
Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.

Either before or after you implement seasons.py, additionally implement, in a file called test_seasons.py, one or more functions that test your
implementation of any functions besides main in seasons.py thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_seasons.py

"""


from datetime import date
import sys
import inflect


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        p = inflect.engine()
        final_result = p.number_to_words(self.year, andword="")
        return f"{final_result.capitalize()} minutes"

    @classmethod
    def get_date(cls):
        try:
            birth_date = input("Date of Birth: ").split("-")
            if len(birth_date) == 1 or len(birth_date) == 2:
                sys.exit("Invalid date")

            # birth_date[0] = year, birth_date[1] = month, birth_date[2] = day
            if date(int(birth_date[0]), int(birth_date[1]), int(birth_date[2])):
                past_date = date(int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))
                today = date.today()
                final_days, final_secs = str(today - past_date).split(",")
                final_days = final_days.split(" ")
                birth_date[1], birth_date[2] = 0, 0
                final_days[0] = int(final_days[0]) * 24 * 60
                return cls(int(final_days[0]), birth_date[1], birth_date[2])

            else:
                sys.exit("Invalid date")

        except ValueError:
            sys.exit("Invalid date")


def main():
    print(Date.get_date())


if __name__ == "__main__":
    main()
