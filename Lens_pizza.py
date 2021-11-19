# You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.
#Here is a listing of all the pizza toppings offered.
toppings = ["pepporoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
print("This is the amount of $2.00 slices of pizza:" + str(num_two_dollar_slices))
#this is how many types of pizza choices there are
num_pizzas = len(toppings)
print("We sell" + str(num_pizzas) + "different kinds of pizza!")
pizza_and_prices = [[2, "pepporoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print("This is the prices of pizza and toppings:" + str(pizza_and_prices))
#This sorts the pizza and prices in ascending order.
pizza_and_prices.sort()
print("This is the pizza sorted in lowest to highest cost:" + str(pizza_and_prices))
#the cheapest pizza is:
cheapest_pizza = pizza_and_prices[0]
print("The cheapest pizza is:" + str(cheapest_pizza))
#the most expensive pizza is:
priciest_pizza = pizza_and_prices[-1]
print("The priciest pizza is:" + str(priciest_pizza))
pizza_and_prices.pop(-1)
print("This is the list of pizza choices with anchovies removed:" + str(pizza_and_prices))
pizza_and_prices.insert(4, [2.5, "peppers"])
print("This is the list of pizza choices with peppers added:" + str(pizza_and_prices))
three_cheapest = pizza_and_prices[:3]
print("These are the three cheapest slices of pizza:" + str(three_cheapest))


