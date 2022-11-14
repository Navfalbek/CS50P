"""
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, 
wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, 
but main is only called if the value of __name__ is "__main__"

Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, 
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_plates.py

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
