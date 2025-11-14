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