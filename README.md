# FINE3300-2026-AI

# FINE 3300 – Assignment 1: Exchange Rate Calculator

## Project Description

This project is a Python based exchange rate calculator that converts amounts between Canadian Dollars (CAD) and US Dollars (USD). It uses exchange rate data from a Bank of Canada CSV file and takes the latest available USD/CAD exchange rate from the last row of the file.

The assignment includes two Python programs: one written by me and another generated using an AI model. Both programs perform the same currency conversions but use different approaches to read and process the exchange rate data.

## Project Files

- **my_Exchange rate.py** – My Python program which uses the pandas library to read the CSV file and perform currency conversions.
- **ExchangeRatesAI.py** – The AI-generated program which uses Python's built-in csv module to read the exchange rate data.
- **BankOfCanadaExchangeRate_2026.csv** – The Bank of Canada exchange rate data used by both programs.

## How the Program Works

1. Reads the exchange rate data from the CSV file.
2. Retrieves the latest available USD/CAD exchange rate.
3. Prompts the user to enter an amount.
4. Asks the user to select the currency to convert from and the currency to convert to.
5. Converts the amount using the exchange rate.
6. Displays the converted amount with dollar signs and two decimal places.

## Currency Conversion

- **USD to CAD:** Multiply the amount by the USD/CAD exchange rate.
- **CAD to USD:** Divide the amount by the USD/CAD exchange rate.

## Tools and Libraries

- Python
- Visual Studio Code
- pandas (used in my program)
- csv module (used in the AI-generated program)
- Git and GitHub

## Running the Programs

Both Python programs require the Bank of Canada CSV file to be in the same folder.

The pandas library must be installed to run my program.

Run either Python file in Visual Studio Code and follow the prompts to enter the amount and currencies.

## Assignment Information

**Course:** FINE 3300 – Python for Finance Professionals

**Assignment:** Assignment 1 – Exchange Rates and Vibe Coding
