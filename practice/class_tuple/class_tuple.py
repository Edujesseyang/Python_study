from collections import namedtuple


my_class = namedtuple(
    'my_class', ['first_class', 'second_class', 'third_class'])

today_class = my_class('ENG10', 'Math1A', 'CIS40')

print(today_class)
