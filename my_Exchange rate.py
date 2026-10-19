import pandas as pd


class ExchangeRates:

    def __init__(self, file_name):
        df = pd.read_csv(file_name)

        # Get the last row's date and USD/CAD exchange rate
        self.date = df.iloc[-1, 0]
        self.usd_to_cad = df["FXAUSDCAD"].iloc[-1]

    def convert(self, amount, from_currency, to_currency):
        if ((from_currency == "USD" or from_currency == "usd") and (to_currency == "CAD" or to_currency == "cad")):
            return amount * self.usd_to_cad
        elif ((from_currency == "CAD" or from_currency == "cad") and (to_currency == "USD" or to_currency == "usd")):
            return amount / self.usd_to_cad
        else:
            return amount 


# Main program
rates = ExchangeRates("BankOfCanadaExchangeRate_2026.csv")

amount = float(input("Enter the amount: "))
from_currency = input("Convert from (USD or CAD): ")
to_currency = input("Convert to (USD or CAD): ")

result = rates.convert(amount, from_currency, to_currency)

print(f"${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")
