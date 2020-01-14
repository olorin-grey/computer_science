# Python project to practice slicing and sorting
toppings = ["cheese", "bacon", "mushrooms", "pepperoni", "pineapple", "sausage",]

prices = [2, 3, 4, 2, 3, 2]

num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizzas.")

# Note: A tuple is an immutable sequence; it cannot be changed.
# If you do not nest zip inside list here, the object in memory will be returned.
# .sort() will compare against the first element in each sublist.
pizzas = list(zip(prices, toppings))
#print(pizzas)


# Sort pizzas so that the pizzas with the lowest price are at the start of the list. 
pizzas.sort()
#print(pizzas)


cheapest_pizza = pizzas[0]

priciest_pizza = pizzas[-1]
#priciest_pizza = pizzas[len(pizzas) - 1]

three_cheapest = pizzas[0:3]
#three_cheapest = pizzas[:3]


num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)

