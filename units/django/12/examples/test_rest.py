import requests

print('Loading data')

API_URL = 'https://django-todoapp.herokuapp.com/api/todos'
response = requests.get(API_URL)
print('Response received: ', response.status_code)

todo_items = response.json()

print('{} items loaded\n'.format(len(todo_items)))

for item in todo_items:
    print('id: {}'.format(item['id']))
    print('title: {}'.format(item['title']))
    print('description: {}'.format(item['description']))
    print('created_at: {}'.format(item['created_at']))
    print('-' * 50)

