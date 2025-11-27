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
def helloWorld(hello, world):
    result = f'{hello} {world}'
    return result

sayHello = helloWorld('hello', 'world')
print(sayHello)