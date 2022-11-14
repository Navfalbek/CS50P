"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. 
In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) 
omitted, whether inputted in uppercase or lowercase.

"""


vowels = 'AaOoUuIiEe'


def main():
     text = str(input("Input: "))
     print(shorten(text))


def shorten(text):
     new_text = ""
     for character in text:
        if character in vowels:
            text = text.replace(character, '')

     return text


if __name__ == "__main__":
     main()
