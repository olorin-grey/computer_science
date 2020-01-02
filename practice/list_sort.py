# Sometimes, we want to sort a list in either numerical or alphabetical. We can 
# use .sort() after calling our list.
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', \n 
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
