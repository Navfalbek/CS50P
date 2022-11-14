"""
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d 
(which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically 
by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

"""


def get_input():
    items_list = {}
    i = 1
    while True:
        try:
            item_input = input()

            item_input = item_input.upper()

            if item_input in items_list:

                i += 1
                # here can be made i string
                items_list[item_input] = i

            else:
                items_list[item_input] = 1

            items_list = dict(sorted(items_list.items())) # this func sortes the dict by value

        except EOFError:
            break

        except KeyError:
            pass
    # print(items_list)
    display(items_list)


def display(items_list):
    for _ in items_list:
        print(items_list[_], _)


get_input()
