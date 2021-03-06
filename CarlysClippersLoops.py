# Demonstration of Loops.
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]
print("These are the original haircut prices: " + str(prices))
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
for price in prices:
  total_price += price
print("Average Haircut Price: " + str(price))
new_prices = [price - 5 for price in prices]
print("These are the new prices for haircuts: " + str(new_prices))
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + "$" + str(total_revenue))
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: " + "$" + str(average_daily_revenue))
cuts_under_30 = [new_prices[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("These are the haircuts under $30: " + str(cuts_under_30))
