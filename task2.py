# Importing http requests module
import requests

# Importing JSON module
import json

# Importing CSV Module
import csv

# Defining http API URL

# http API call to check market status (http GET method)
url_market = "https://forex.1forge.com/1.0.3/market_status?api_key=DkYnPOL1hIqzNublNZsdyz3Lw71L8WJM"

# http API check for currency pairs (http GET method)
url_symbols = "https://forex.1forge.com/1.0.3/symbols?api_key=DkYnPOL1hIqzNublNZsdyz3Lw71L8WJM"

headers = {
    'cache-control': "no-cache",
    'Postman-Token': "b89f3332-b07b-42de-8c54-3d3ff31b4cfe"
    }

# Store API Response to variables below
response_market = requests.request("GET", url_market, headers=headers)
response_symbols = requests.request("GET", url_symbols, headers=headers)

# Print market status (Open/Closed)
print(response_market.text)

# Convert JSON response and store currency_pairs as a list
currency_pairs = json.loads(response_symbols.text)


# Store first 10 symbols from currency_pairs list into firstTen
firstTen = []
firstTen = currency_pairs[0:10]

#
file_list = []

# # # Open a file for writing
file_data = open('zop_test.csv', 'w')
# # # # Create CSV writer object
csv_writer = csv.writer(file_data)
# loop through list of items
csv_writer.writerow(['symbol, bid, ask, price, timestamp'])
for element in firstTen:
    # http API to check for quotes (http GET method)
    url_quotes = "https://forex.1forge.com/1.0.3/quotes?pairs=" + element + "&api_key=DkYnPOL1hIqzNublNZsdyz3Lw71L8WJM"
    response_quotes = requests.request("GET", url_quotes, headers=headers)

    # load Json data into List of dictionaries - returns a list [ ]
    data_list = json.loads(response_quotes.text)

    # to extract first item in List of dictionary - returns a dictionary { }
    data_dict = data_list[0]        # access the first item in data list

    # Write values to file .csv
    csv_writer.writerow(data_dict.values())
file_data.close()






