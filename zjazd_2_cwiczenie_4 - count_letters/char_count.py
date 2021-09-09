"""
Napisz program który policzy liczbę liter w danym stringu.

my_string = "The quick brown fox jumps over the lazy dog"

"""

# example_dict = {'a': 1, 'b': 2, 'c': 3}
# example_dict['a']

# example_dict.get('a')

# example_dict['c'] = 1   - Adding key with value into dict


my_string = "The quick brown fox jumps over the lazy dog"
my_dict = {}

my_string = my_string.lower()
for char in my_string:
    print(char)
    if char in my_dict:
        my_dict[char] += 1
    else:
        my_dict[char] = 1
    print(my_dict)
    print(10* '*')
print(my_dict)

