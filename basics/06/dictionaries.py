# dictionaries contain keyed values, for example below is car_0,
# a black honda civic
# there is no limit to key values in a dictionary.
car_0 = {'color': 'black','brand': 'honda',
         'model': 'civic'}


# each value, for example 'brand' has a value attribute that can
# be accessed by index or by invoking its index through an element
print(car_0['model'])
new_car = car_0['brand']
print(f'I just bought a new {new_car.title()}')


# key values can be added at any time by defining them on the fly
print(f'\n{car_0}')

car_0['price'] = '$5,000'

print(car_0)


# empty dictionaries can be convenient or needed.
car_0 = {}

car_0['color'] = 'blue'
car_0['model'] = 'subaru'

print(f'\n{car_0}')


# using same syntax, keys and values can be modified.
car_0['model'] = 'mitsubishi'

print(f'\n{car_0}')

# a more complex usage of modifying dictionary values for
# specific purposes
car_0['condition'] =  'new'
car_0['mileage'] = 0
mileage = 25000

print(f'\n{car_0['condition']}')
car_0['mileage'] = mileage

if car_0['mileage'] > 20000:
    car_0['condition'] = 'used'
print(car_0['condition'])

# to remove key-value pairs
del car_0['condition']
print(f'\n{car_0}')

# get() is used as a default value to be returned if a value does
# not exist. This topic will be covered further in ./10
car_value = car_0.get('nothing', 'nothing to see here.')
print(f'\n{car_value}')
