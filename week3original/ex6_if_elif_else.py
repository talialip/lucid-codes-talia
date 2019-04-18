from example_data import lucid_codes

# DATA
example = {
    'students': ['Aaron', 'Alexa', 'Apurva', 'Ayesha', 'David F.', 'David M.', 'Fion', 'Grace', 'Julia', 'Leah', 'Manu', 'Mattie', 'Navneet', 'Talia', 'Wilson', 'Brian', 'Chloe', 'Jimmy'],
    'trainers': ['Alex', 'Hannah', 'Justin', 'Kyle', 'Marcus', 'Marina', 'PJ', 'Ben', 'Eric', 'Neil', 'Steven']
}

# CONTROL FLOW
name = input('Please enter a name: ')
if name in example['students']:
    print(name + ' is a Lucid Codes student.')
elif name in example['trainers']:
    print(name + ' is a Lucid Codes instructor.')
else:
    print('PythonBot does not know this individual.')
