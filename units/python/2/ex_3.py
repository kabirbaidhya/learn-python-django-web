# Program to ask for the date of birth
# and calculate the user's age.

dob = input('Enter your Date of Birth(yyyy-mm-dd): ')
dob = dob.split('-')

# Calculate the date timestamp in years.
dob_timestamp = float(dob[0]) + float(dob[1])/12 + float(dob[2])/365

# Calculate the today's timestamp in years.
today = ['2017', '03', '17']
today_timestamp = float(today[0]) + float(today[1])/12 + float(today[2])/365

# Compute the difference
years = today_timestamp - dob_timestamp
months = (years - int(years)) * 12

print('Your age is %d years %d months' % (years, months))
