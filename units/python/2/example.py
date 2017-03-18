s = input('Enter a string: ')

print("No. of characters = %d" % len(s))
print("First Character = %s" % s[0])
print("Last Character = %s" % s[len(s) - 1])

# Count the number of vowels
print("No. of 'a' = %s" % s.count('a'))
print("No. of 'e' = %s" % s.count('e'))
print("No. of 'i' = %s" % s.count('i'))
print("No. of 'o' = %s" % s.count('o'))
print("No. of 'u' = %s" % s.count('u'))

# Calculate Percentage of vowels
total_vowels = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
percentage = (float(total_vowels) / len(s)) * 100
print("%.2f%% are vowels." % percentage)
