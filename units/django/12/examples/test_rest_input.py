import requests

API_URL = 'https://django-todoapp.herokuapp.com/api/todos'-

print('Enter todo details:\n')
title = input('Title: ')
description = input('Description: ')
user = input('User Id: ')

print('Creating a new user...')

result = requests.post(API_URL, data = {
    'title': title,
    'description': description,
    'user': user
})
