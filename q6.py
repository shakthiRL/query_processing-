import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt

# Define the start and end dates
start_date = '2023-01-01'
end_date = '2023-12-31'

# Fetch historical stock prices for Alphabet Inc. (GOOGL)
alphabet_stock_data = pdr.get_data_yahoo('GOOGL', start=start_date, end=end_date)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(alphabet_stock_data['Volume'], alphabet_stock_data['Close'], alpha=0.5)
plt.title('Trading Volume vs Stock Prices of Alphabet Inc. (GOOGL)')
plt.xlabel('Trading Volume')
plt.ylabel('Stock Price (USD)')
plt.grid(True)

# Show the plot
plt.show()
