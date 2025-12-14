# to initiate a function
# the parameter name defines the function
def greet():
    print('Hello!')
    
greet()

# data can be passed through by adding an arguement
# within the enclosed brackets of the parameter
def greet_user(user):
    print(f'Hello, {user.title()}')

# in this case 'james' is the arguement being passed
# through to greet_user()
greet_user('james')

# personal arguements are based on the order of arguements provided
# arguements can have default values declared
def takeMeasurement(measuredItem, heightInFeet, widthInFeet, measurementType='ft.'):
    print(f'The {measuredItem} is {heightInFeet} {measurementType} tall, by {widthInFeet} {measurementType} wide.')

# default value will take effect because value was not provided
takeMeasurement(8, 'wall', 12)

# keywords arguements can be used to prevent confusion in declaration
takeMeasurement(measuredItem='wall', heightInFeet=8, widthInFeet=12, measurementType='Meters')
# returning a value from the function
def createPerson(firstName, lastName, middleName='', age='None'):
    # validating that middle name is present
    if middleName == '':
        # return appropriate person object  based on presence of middlename
        person = {'first': firstName, 'last': lastName, 'age': age}
    else:
        person = {'first': firstName, 'middle': middleName, 'last': lastName, 'age': age}
        
    if age:
        person['age'] = age
    return person

# create value as returned value of helloWorld function
noMiddleName = createPerson('Beetee', 'Latier')
hasMiddleName = createPerson('Steve', 'Robin', 'Renolds', age=36)
print(noMiddleName)
print(hasMiddleName)

# while loops allow code to execute only while a condition is true
# this code is blocked out because if not it would loop infinitely
'''
while True:
    print('\nYour username please?')
    print('\nTo quit press "q"')
    username = input('username: ')
    if username == 'q':
        break

    user = greet_user(username)

    print(f'Ah, yes. Welcome back {user}!')
'''

# 12-13-2025 CH08 PG142