from pprint import pprint
dict_numbers = [{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(0, 16)]
# TODO решить с помощью list comprehension и распечатать его


pprint(dict_numbers)
