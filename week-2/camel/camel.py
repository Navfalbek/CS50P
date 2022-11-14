"""
In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, 
whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable
for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name 
(e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), 
with all letters in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs 
the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

"""


def camelCase():
    camel_text = str(input("camelCase: "))
    snake_case(camel_text)


def snake_case(camel_text):
    for character in camel_text:
        if character >= "A" and character <= "Z":

            # working with ASCII code. adding 32 to the character ASCII code to make it lower case
            character_lower = chr(ord(character) + 32)
            character_lower = "_" + character_lower

            camel_text = camel_text.replace(character, character_lower)

    print("snake_case: ", camel_text)

camelCase()
