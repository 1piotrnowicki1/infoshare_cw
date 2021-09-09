my_string = "The quick brown fox jumps over the lazy dog"
my_dict = {}

my_string = my_string.lower()
my_string = my_string.replace(' ', '')
print(my_string)
for char in my_string:
    if char not in my_dict:
        my_dict[char] = my_string.count(char)
print(my_dict)
