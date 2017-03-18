names = ['John Doe', 'Jane Doe', 'Johnny Turk']
# Change the first name in the list
names[0] = 'Foo Bar'
print('Names now:', names)

# Append some more names
names.append('Molly Mormon')
names.append('Joe Bloggs')
print('Names finally:', names)
print('Last name in the list: %s' % names[-1])

# You can join lists using str.join() method
joined_names = '\n'.join(names)
print('\nList of names:')
print(joined_names)
