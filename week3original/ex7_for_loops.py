from example_data import lucid_codes

for student in lucid_codes['students']:
    print('Students name is: ' + student['name'])
    print('Students title is: ' + student['title'])
    print()

# Counting always starts at 0
for count in range(len(lucid_codes['students'])):
    if count + 1 == 1:
        ending = 'st'
    elif count + 1 == 2:
        ending = 'nd'
    elif count + 1 == 3:
        ending = 'rd'
    else:
        ending = 'th'

    print(lucid_codes['students'][count]['name'] + ' is the ' + str(count + 1) + ending + ' student.')
