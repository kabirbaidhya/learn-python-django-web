def get_adder_of(a = 1):
    return lambda x: x + a

add_five = get_adder_of(5)
add_two = get_adder_of(2)
add_seven = get_adder_of(7)

print('10 + 5 = %d' % add_five(10))
print('8 + 2 = %d' % add_two(8))
print('8 + 7 = %d' % add_seven(8))

