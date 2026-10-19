import pandas as pd  # Import pandas to read the CSV file


class ExchangeRates:

    def __init__(self, file_name):
        # Read the exchange rate data from the CSV file
        df = pd.read_csv(file_name)

        # Get the last row's date and USD/CAD exchange rate
        self.date = df.iloc[-1, 0]
        self.usd_to_cad = df["FXAUSDCAD"].iloc[-1]

    def convert(self, amount, from_currency, to_currency):
        # Convert USD to CAD by multiplying by the exchange rate
        if ((from_currency == "USD" or from_currency == "usd") and (to_currency == "CAD" or to_currency == "cad")):
            return amount * self.usd_to_cad

        # Convert CAD to USD by dividing by the exchange rate
        elif ((from_currency == "CAD" or from_currency == "cad") and (to_currency == "USD" or to_currency == "usd")):
            return amount / self.usd_to_cad

        # Return the original amount if neither condition is met
        else:
            return amount


# Main program

# Create an ExchangeRates object using the CSV file
rates = ExchangeRates("BankOfCanadaExchangeRate_2026.csv")

# Ask the user to enter the amount and currencies
amount = float(input("Enter the amount: "))
from_currency = input("Convert from (USD or CAD): ")
to_currency = input("Convert to (USD or CAD): ")

# Convert the amount using the exchange rate
result = rates.convert(amount, from_currency, to_currency)

# Display the result with dollar signs, commas, and two decimal places
print(f"${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")