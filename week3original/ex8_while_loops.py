from example_data import lucid_codes

# i is a commonly used variable for iterating over loops
i = 0
while i < len(lucid_codes['trainers']):
    print(lucid_codes['trainers'][i])
    i = i + 1

print()

running = True
while running:
    user_input = input('What would you like to capitalize? ')
    if user_input == 'quit':
        running = False
    else:
        print(user_input.upper())
