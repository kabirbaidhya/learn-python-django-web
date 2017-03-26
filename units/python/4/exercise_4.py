authorized_users = [
    {
        'name': 'John Doe',
        'email': 'johndoe@example.com',
        'password': 'aaa'
    },
    {
        'name': 'Admin',
        'email': 'admin@example.com',
        'password': 'admin'
    }
]

def main():
    email = input('Enter Email: ')
    password = input('Enter Password: ')

    print()

    (user_exists, login_sucess) = check_login(email, password)

    # If user doesn't exist then let him know.
    if user_exists == False:
        print('User with email {} does not exist in our system.'.format(email))
    
    # If login_sucess is still false, show the error.
    if login_sucess == False:
        print('Access Denied')
       

def check_login(email, password):
    login_sucess = False
    user_exists = False
    
    for user in authorized_users:
        # Check if the combination of email and password matches
        if email == user['email'] and password == user['password']:
            login_sucess = True
            print('User found:') 
            print('Name: {}'.format(user['name']))
            print('Email: {}'.format(user['email']))
            break
    
        # But if the user's email exists
        elif email == user['email']:
            user_exists = True
    
    return (login_sucess, user_exists)

# Start the program            
main()
