import quandl
import pandas as pd
import matplotlib.pyplot as plt

# API Key for quandl. To run this program, save your API key in a file named 'my_api_key.txt' and place the file in the
# same directory as this one.
with open('my_api_key.txt') as file_object:
    my_api_key = file_object.read().strip()

# Dataframe storing the historical daily closing prices or ZO1_X
eon_data = quandl.get("FSE/ZO1_X.4", authtoken=my_api_key)

# List that will store the closing share price of each business day for the last 2 years
close_prices = []
# List that will store the 200MA of each business day for the last 2 years
moving_averages = []

# For loop to calculate the moving averages for the last two years, storing them in reverse chronological order
for i in range(0, 731):
    close_price = eon_data.iloc[-i - 1, 0]
    close_prices.append(close_price)
    tot = 0
    for j in range(0, 200):
        tot += eon_data.iloc[-i - j, 0]

    moving_average = tot / 200
    moving_averages.append(moving_average)

# Places the close prices in chronological order
close_prices.reverse()
# Places the moving averages in chronological order
moving_averages.reverse()

# Based on the most recent moving average and share price, tells the user whether they should be looking to buy or sell

# Case where price is higher than moving average
if close_prices[-1] > moving_averages[-1]:
    print("The share price is currently higher than the moving average. Therefore, you should look to buy.")
else:
    print("The share price is currently lower than the moving average. Therefore, you should look to sell.")

# Plot a graph showing the moving average and share price over the last 2 years
plt.plot(moving_averages)
plt.plot(close_prices)
plt.ylabel("Share price")
plt.xlabel("Day (Most recent day last)")
plt.legend(('200-Day Moving Average', 'Closing Share Price'))
plt.show()



