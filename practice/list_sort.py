# Sometimes, we want to sort a list in either numerical or alphabetical. We can 
# use .sort() after calling our list.
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace',
             '1600 Pennsylvania Ave', '10 Downing St.']

addresses.sort()
print(addresses)


names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()
print(names)



# .sort() modifies the original list and returns None
# https://docs.python.org/2/tutorial/datastructures.html
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()
print(sorted_cities)
#Output = None



# A second way of sorting a list is to use sorted. sorted is different from .sort() 
# in several ways:
# - It comes before a list, instead of after
# - It generates a new list
names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']

sorted_names = sorted(names)
print(sorted_names)


games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

games_sorted = sorted(games)
print(games, games_sorted)

