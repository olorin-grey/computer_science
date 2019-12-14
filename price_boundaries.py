# This function takes in two parameters for price boundaries
def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = margin + target
  return low_limit, high_limit

# Now we call the function and save the returned values
# in the variables called low and high.
low, high = get_boundaries(100, 20)
print(low)
print(high)


'''
Template reference:
def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2

x_squared, y_squared = square_point(1, 3)
print(x_squared)
print(y_squared)
'''
