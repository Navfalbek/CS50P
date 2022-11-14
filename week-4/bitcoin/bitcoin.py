"""
In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, , that they would like to buy. 
If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.

Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions

Outputs the current cost of  Bitcoins in USD to four decimal places, using , as a thousands separator.

"""


import requests
import sys
import json

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        x = float(sys.argv[1])

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        # print(json.dumps(response.json(), indent = 2))
        o = response.json()
        rate = o["bpi"]["USD"]["rate_float"]
        amount = x * rate

        # print(o["bpi"]["USD"]["rate_float"])
        print(f"${amount:,}")

except requests.RequestException:
    sys.exit("Exited with requests.RequestException")
except ValueError:
    sys.exit("Command-line argument is not a number")
