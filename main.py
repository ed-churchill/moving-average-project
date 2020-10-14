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
    close_prices.append(eon_data.iloc[-i - 1])
    tot = 0
    for j in range(0, 200):
        tot += eon_data.iloc[-i - j, 0]

    moving_average = tot / 200
    moving_averages.append(moving_average)

# Places the close prices in chronological order
close_prices.reverse()
# Places the moving averages in chronological order
moving_averages.reverse()
print(moving_averages)

plt.plot(moving_averages)
plt.plot(close_prices)
plt.ylabel("Share price")
plt.legend(('200-Day Moving Average', 'Closing Share Price'))
plt.show()


