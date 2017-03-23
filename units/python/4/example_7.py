names = ['John Doe', 'Jane Doe', 'Johnny Turk', 'Molly Mormon']
i = 0
total_names = len(names)
print('Users:')

while i < total_names:
    
    # This is same as doing. 
    #
    # if i == total_names - 2:
    #     end = ' and\n'
    # else:
    #     end = '\n'
    end = ' and\n' if i == total_names - 2 else '\n'

    print(' - %s' % names[i], end=end)
    i += 1


