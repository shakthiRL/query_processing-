import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt

# Define the start and end dates
start_date = '2023-01-01'
end_date = '2023-12-31'

# Fetch historical stock prices for Alphabet Inc. (GOOGL)
stock_data = pdr.get_data_yahoo('GOOGL', start=start_date, end=end_date)

# Create a bar plot for the trading volume
stock_data['Volume'].plot(kind='bar', title='Trading Volume of Alphabet Inc. (GOOGL)', 
                           xlabel='Date', ylabel='Volume', 
                           grid=True, figsize=(14, 7))

# Show the plot
plt.show()

