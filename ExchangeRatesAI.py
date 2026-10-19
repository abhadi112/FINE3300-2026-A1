# ExchangeRatesAI.py
# FINE 3300 - Python for Finance Professionals
# Currency exchange rate calculator (USD <-> CAD) using Bank of Canada data.

import csv  # built-in module for reading CSV files


class ExchangeRates:
    """Reads a Bank of Canada exchange rate file and converts between USD and CAD."""

    def __init__(self, filename):
        # Store the file name and read the latest USD/CAD rate from it
        self.filename = filename
        self.usd_cad = self.read_latest_rate()

    def read_latest_rate(self):
        """Return the USD/CAD rate from the last row of data in the file."""
        # utf-8-sig removes the hidden byte-order mark at the start of the file
        with open(self.filename, newline="", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            header = next(reader)        # first row holds the column names
            rows = list(reader)          # remaining rows hold the data

        # Find the USD/CAD column (named "FXAUSDCAD" in this file)
        usd_col = None
        for i, name in enumerate(header):
            if "USDCAD" in name:
                usd_col = i

        # The latest rate is in the last row of data
        latest_row = rows[-1]
        self.latest_date = latest_row[0]  # first column is the date
        return float(latest_row[usd_col])

    def convert(self, amount, from_currency, to_currency):
        """Convert an amount from one currency (USD or CAD) to the other."""
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == to_currency:
            return amount                    # no conversion needed
        elif from_currency == "USD" and to_currency == "CAD":
            return amount * self.usd_cad     # USD -> CAD: multiply by the rate
        else:
            return amount / self.usd_cad     # CAD -> USD: divide by the rate


# ---------------- Main program ----------------
if __name__ == "__main__":
    # Bank of Canada CSV file (must be in the same folder as this script)
    rates = ExchangeRates("BankOfCanadaExchangeRate_2026.csv")

    # Ask the user for the amount and the two currencies
    amount = float(input("Enter the amount: "))
    from_currency = input("From currency (USD or CAD): ").upper()
    to_currency = input("To currency (USD or CAD): ").upper()

    # Do the conversion
    result = rates.convert(amount, from_currency, to_currency)

    # Display the result rounded to the nearest penny with $ signs and currency codes
    print(f"\nUsing USD/CAD rate of {rates.usd_cad} ({rates.latest_date}):")
    print(f"${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")
