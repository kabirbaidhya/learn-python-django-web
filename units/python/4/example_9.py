# Lists and the for loop
names = ['John Doe', 'Jane Doe', 'Johnny Turk', 'Molly Mormon']
print('Users:')

for name in names:
    end = ' and\n' if name == names[-2] else '\n'

    print(' - %s' % name, end=end)

