# Stock Data Scraper

This is a Python script that scrapes real-time stock market data from [MeroLagani](https://merolagani.com/LatestMarket.aspx) and saves the extracted data into a CSV file. The script retrieves stock information such as stock names, prices, and other relevant data, providing a simple way to collect and analyze live trading data.

## Features

- Scrapes stock data from the MeroLagani website.
- Extracts relevant columns, including stock name, price, etc.
- Handles missing data by padding rows with empty strings.
- Saves the extracted data into a CSV file for further analysis.

## Requirements

Before running the script, ensure that you have the following Python libraries installed:

- `requests`
- `beautifulsoup4`
- `pandas`

You can install them using `pip`:

```bash
pip install requests beautifulsoup4 pandas
