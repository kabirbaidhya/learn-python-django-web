age = int(input('Enter age: '))

if age <= 0:
    print('Invalid age')
elif age <= 1:
    print("You're an infant")
elif age <= 12:
    print('You\'re just a kid.')
elif age <= 19:
    print('You\'re a teenager.')
elif age <= 45:
    print('You are adult now.')
elif age <=59:
    print('You are middle-aged.')
elif age <= 120:
    print('You are old now.')
else:
    print('You\'re too old to still be alive.')


