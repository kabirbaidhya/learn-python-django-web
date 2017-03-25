data = [
    {
        'name': 'Kabir Baidhya',
        'email': 'kabirbaidhya@gmail.com'
    },
    {
        'name': 'John Doe',
        'email': 'johndoe@example.com'
    },
    {
        'name': 'John Doe',
        'email': 'johndoe@example.com'
    },
    {
        'name': 'John Doe',
        'email': 'johndoe@example.com'
    }
]

for (i, item) in enumerate(data):
    print('\nUser %d' % (i + 1))
    print('Name: %s' % item['name'])
    print('Email: %s' % item['email'])

