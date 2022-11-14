"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and 
ignore any integer that isn’t an accepted denomination.

"""


def coke_machine():
    price = 50

    while True:

        print(f"Amount due: {price}")

        insert_coin = int(input("Insert coin: "))

        if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
            price -= insert_coin
            price = abs(price)

        else:
            # continue
            price = price

        if price <= 0:
            break
        # if price < 0:

    price = abs(price)
    print(f"Amount price: {price}")

coke_machine()
