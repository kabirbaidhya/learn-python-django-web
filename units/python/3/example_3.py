# You can even create new lists by processing existing lists.
words = ['this', 'is', 'just', 'a', 'test']
capitalized_words = [x.capitalize() for x in words]

print('Words:', words)
print('Capitalized Words:', capitalized_words)

# Can use it for filtering the list items as well.
words = ['hello', 'world', 'foo', 'bar', 'test', 'python', 'is', 'awesome']
short_words = [x for x in words if len(x) <= 3]
other_words = [x for x in words if x not in short_words]
words_with_e = [x for x in words if x.count('e') >= 1]

print('Words:', words)
print('Short Words:', short_words)
print('Other Words:', other_words)
print('Words with "e":', words_with_e)
