# Making a global variable for premium shipping since it is a flat rate
shipping_premium = 125.00


def shipping_ground(weight):
  
  if (weight <= 2):
    price_per_pound = 1.50
  elif (weight <= 6):
    price_per_pound = 3.00
  elif (weight <= 10):
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75

  return 20 + (price_per_pound * weight)

# Testing the function
#print(ground_shipping(8.4))
# should print out 53.60


def shipping_drone(weight):
  
  if (weight <= 2):
    price_per_pound = 4.50
  elif (weight <= 6):
    price_per_pound = 9.00
  elif (weight <= 10):
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25

  return price_per_pound * weight

# Testing the function
#print(drone_shipping(1.5))
# should print out 6.75


def ship_cheapest_method(weight):

  ground = shipping_ground(weight)
  premium = shipping_premium
  drone = shipping_drone(weight)

  if (ground < premium) and (ground < drone):
    method = "standard ground"
    cost = ground
  elif (premium < ground) and (premium < drone):
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone

  return(
    "The cheapest shipping option available is $%.2f with %s shipping."
    % (cost, method) 
    )

# Testing the project  
#print(ship_cheapest_method(4.8))
#print(ship_cheapest_method(41.5))
