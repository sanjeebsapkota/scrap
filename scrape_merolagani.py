import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website
url = "https://merolagani.com/LatestMarket.aspx"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table containing the stock data
    table = soup.find('table', class_='table table-hover live-trading sortable')
    
    # Extract table headers
    headers = []
    for th in table.find_all('th')[:9]:  # Only take the first 9 headers
        headers.append(th.text.strip())
    
    # Extract table rows
    rows = []
    for tr in table.find_all('tr')[1:]:  # Skip the header row
        row = [td.text.strip() for td in tr.find_all('td')]
        if len(row) < 9:  # If the row has fewer than 9 columns
            row.extend([''] * (9 - len(row)))  # Pad with empty strings
        rows.append(row)
    
    # Create a DataFrame using the extracted data
    df = pd.DataFrame(rows, columns=headers)
    
    # Save the data to a CSV file in the specified location
    df.to_csv(r'C:\Users\Dell\Desktop\New folder\stock_data.csv', index=False)
    
    print("Data saved to C:\\Users\\Dell\\Desktop\\New folder\\stock_data.csv")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")