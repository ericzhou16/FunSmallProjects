"""
Doing currency conversion with data from API. Trying to learn more about working with APIs and sending requests.

Heavily based on code from: youtube.com/watch?v=txKBWtvV99Y
"""
from requests import get
from pprint import PrettyPrinter

# URLs
BASE_URL = "https://free.currconv.com/"
API_KEY = "062e425db21c43fb2b08"

# Pretty printer to print JSON nicely
printer = PrettyPrinter()


# Get sorted list of currencies
def get_currencies():
    # Url request
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint

    # Getting currencies data
    data = get(url).json()['results']

    # List out all the currencies and sort them
    data = list(data.items())
    data.sort()
    return data


# Print all currencies out in a nice formatting
def print_currencies(currencies):
    for symbol, currency in currencies:
        symbol = currency.get("currencySymbol", "")
        print(f"{currency['id']} - {currency['currencyName']} - {symbol}")


# Getting an exchange rate between 2 currencies
def exchange_rate(currency1, currency2):
    # Url request
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    # Invalid edge case check
    if not data:
        print('Invalid currencies.')
        return

    # Getting rate and formatted print
    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")
    return rate


# Calculate conversion between 2 currencies
def convert(currency1, currency2, amount):
    # Getting rate
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    # Invalid edge case
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    # Conversion and formatted print
    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount


# Main function that can do anything with currencies
def main():
    # Getting currencies
    currencies = get_currencies()

    # Instructions
    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    # Infinite loop of following instructions
    while True:
        # Input command
        command = input("Enter a command (q to quit): ").lower()

        # Checking command
        if command == "q":  # quit
            break
        elif command == "list":  # list currencies
            print_currencies(currencies)
        elif command == "convert":  # convert currencies
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":  # conversion rate for currencies
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:  # unrecognized command edge case
            print("Unrecognized command!")


# Calling main function
main()
