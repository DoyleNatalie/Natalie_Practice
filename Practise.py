

import pandas as pd
Netflix_shows=pd.read_csv("Netflix Shows.csv")

print(Netflix_shows.info())
print(Netflix_shows.head())

print(8 / 2)

# Example 2, do not modify!
print(2**2)

revenue_1 = 258
revenue_2 = 84
revenue_3 = 126


# Print the total revenue
total = revenue_1 + revenue_2 + revenue_3
print(total)

# Create and print list names
names = [ 'Apple Inc', 'Coca-Cola','Walmart',]
print(names)

# Create and print list prices
prices = [159.54, 37.13, 71.17]
print(prices)

# Print the first item in names
print(names[0])

# Print the second item in names
print(names[1])

# Print the last element in prices
print(prices[-1])

# Print the average revenue
average = total / 3
print(average)


austin=pd.read_csv("austin_weather.csv")
seattle=pd.read_csv("seattle_weather.csv")

fig,ax =plt.subplots()
plt.show()

fig, ax.plot(austin["DATE"],austin["MLY-CLDD-BASE50"])
fig, ax.plot(seattle["DATE"],seattle["MLY-CLDD-BASE50"])
plt.show()

