birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
HEAD
    'Rowan Atkinson': '01/6/1955',
    'Massimo XXXXX': '02/12/1998',
    'AAA BBB': '14/03/2000'
=======
    'Rowan Atkinson': '01/6/1955'
    'Massimo Xxxxx': '02/12/1998'
>>>>>>> main
}

def print_birthdays():
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name):
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

