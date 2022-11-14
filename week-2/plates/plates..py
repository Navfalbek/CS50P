"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead
of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements 
and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()
    if (("A" <= s[0] <= "Z") and ("A" <= s[1] <= "Z")) and (len(s) >= 2 and len(s) <= 6):

        if s.__contains__(".") or s.__contains__(" "):
            return False
        else:
            middle_string = s[1:-1]

            if middle_string.isnumeric() and middle_string.find(0):
                return False

            first_index = s.find("0") - 1

            if s[-first_index].isdigit():
                for var in s:
                    if var.isdigit():
                        if var.startswith("0"):
                            return False
                        else:
                            return True


            if s[-2].isdigit() and s[-1].isdigit():
                return True
            elif s[-2].isdigit():
                return True
            elif s.isalpha():
                return True

    else:
        return False

if __name__ == "__main__":
    main()
