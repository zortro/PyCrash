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
car_0['model'] = 'impreza'

print(f'\n{car_0}')


# using same syntax, keys and values can be modified.
car_0['model'] = 'eclipse'

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
print(f'\n{car_value}\n')

# looping all keys and values requires the key and its value
# be defined within the loop request
# NOTE: the key and values can be given any names as long as
# syntax is followed
for key, value in car_0.items():
    print(f'Key: {key}')
    print(f'value: {value}')
print('\n')
    
# dictionaries loop outputs can be filtered by key via the
# key() method
for k in car_0.keys():
    print(f'Key: {k}')

# values can be filtered as well using the values() method
print('\nThe following are values found within `car_0`:')
for v in car_0.values():
    print(v)
print('\n')

# consider a value shows up more than once
car_0['brand'] = 'mitsubishi'
car_0['maker'] = 'mitsubishi'
print(f'{car_0}\n')

# to check for repeats the set() function can be used to pull
# out the unique values
for v in set(car_0.values()):
    print(v)
print('\n')

# by default a dictionary will loop through key values if not
# defined
for k in car_0:
    print(f'Key: {k}')
print('\n')

# if statements can be utilized via the keys() method aswell
query = ['mileage', 'owners', 'color']
for k, v in car_0.items():
    if k in query:
        print(f'{k}: {v}')
print('\n')

# using the sorted function will return the keys in the 
# dictionary in order
for k in sorted(car_0.keys()):
    print(f'key: {k}')
print('\n')

# dictionaries can be nested within lists
car_1 = {'brand': 'honda', 'color': 'red',
         'maker': 'honda', 'mileage': 5000,
         'model': 'civic'}

car_2 = {'brand': 'toyota', 'color': 'white',
         'maker': 'toyota', 'mileage': 125000,
         'model': 'avalon'}

cars = [car_0, car_1, car_2]

for car in cars:
    print(car)
print('\n')

# create a lot of 10 cars with 5 of each model
lot = []

for number in range(5):
    new_car = {'brand': 'honda', 'color': 'red',
         'maker': 'honda', 'mileage': 5000,
         'model': 'civic'}
    lot.append(new_car)
    
print('\n')

for number in range(5):
    new_car = {'brand': 'kia', 'color': 'green',
         'maker': 'honda', 'mileage': 5000,
         'model': 'civic'}
    lot.append(new_car)
print('\n')

# the values of a range within the list can be adjusted

for cars in lot[3:7]:
    if cars['color'] == 'red':
        cars['color'] = 'orange'
    elif cars['brand'] == 'kia':
        cars['brand'] = 'toyota'
        cars['model'] = '4runner'
        cars['color'] = 'blue'

# show lot
for car in lot:
    print(car)
    
# dictionary containing pizza and it's toppings using nested
# key pairs
pizza = {
    'crust': 'stuffed',
    'toppings': ['pepperoni', 'cheese', 'sausage'],
}

# lists all toppings stored in key of toppings within pizza
# dictionary
for topping in pizza['toppings']:
    print(f"your pizza will have {topping}")
    
# dict containing people's favorite languages
favorite_languages = {
'jen': ['python', 'rust'],
'sarah': ['c'],
'edward': ['rust', 'go'],
'phil': ['python', 'haskell'],
}

# displays individuals lists of favorite languages
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f'\t{language.title()}')
        
# dictionaries can be built within one another
# it can be messy but can be used circumstancially
users = {
    'fakeAcc' : {
        'password' : 'Unsecure123',
        'email' : 'example@example.com'
    },
    'tippyTwo' : {
        'password' : 'iLoveMyShihTzu',
        'email' : 'tippy@two.com'
    }
}

for user, info in users.items():
    print(f'\nuser: {user} data:')
    password = f'{info['password']}'
    email = f'{info['email']}'
    print(f'\tpassword: {password}')
    print(f'\temail: {email}')