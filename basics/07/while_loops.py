# a while loop can be used to count through a series of
# numbers
index = 1
while index <= 5:
    print(index)
    index += 1
    
# the following will repeat any message that is not
# 'exit'
prompt = '\nWhatever is entered will be repeated:'
prompt += '\nEnter "exit" to end.\n'

# flags can monitor whether or not a program should
# continue to run based on multiple conditions
active = True

while active:
    message = input(prompt)
    if message == 'exit':
        active = False
    else:
        print(message)
        
prompt = '\nEnter the name of pets you own:'
prompt += '\n(enter "exit" when ready to end prompt.)\n'

animals = []

while True:
    animal = input(prompt)
      
    if animal == 'exit':
        
        # break can be used to exit a loop
        if len(animals) == 1:
            print(f'Your house has {len(animals)} animal!')
            break
        else:
            print(f'Your household has {len(animals)} animals!')
            break
    else:
        print(f'added {animal.title()}')
        animals.append(animal)
        
# every loop needs an end so it wont continue forever
# if break was not present this code would run forever
x = 1
while x <= 5:
    print(x)
    break

# list items can be moved among various lists
unconfirmed = ['marceline', 'fin', 'jake', 'simon',
               'margles']
confirmed = []

while unconfirmed:
    # move last user in unconfirmed to current
    current = unconfirmed.pop()

    print(f'Verifying {current}...')
    if current != 'margles':
        confirmed.append(current)
    else:
        print(f'Could not confirm {current}')
print('\nThe following users were confirmed')
for user in confirmed:
    print(user.title())

# to remove all instances of a specific value from a list
# remove() can be called
pets = [
    'dog', 'dog', 'cat', 'fish',
    'rabbit'
]

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# additionally user input can be stored in a dictionary
responses = {}

# set polling as active
polling = True

while polling:
    # Store persons name and response
    name = input('\nWhat is your name?\n')
    response = input('Where were you born?\n')
    
    # Store name response keypair in dictionary
    responses[name] = response
    
    repeat = input('Would you like to take another poll?\n')
    if repeat == 'no':
        polling = False
        
print('\n--== Results ==--')
for name, response in responses.items():
    print(f'{name} was born in {response}')