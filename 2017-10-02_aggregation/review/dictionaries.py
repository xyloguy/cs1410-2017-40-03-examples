
import random, sys

r = random.randint

def meow(times):
    s = ''
    for i in range(times):
        s += 'meow '
    return s.strip()

def woof(times):
    s = ''
    for i in range(times):
        s += 'woof '
    return s.strip()

def oink(times):
    s = ''
    for i in range(times):
        s += 'oink '
    return s.strip()

def quit(times):
    sys.exit(0)

def sound(choice):

    choices = {
        'c': meow,
        'd': woof,
        'p': oink,
        'q': quit
    }

    if choice in choices:
        a = input('how many times (r for random): ')
        if a == 'r':
            a = r(0,10)
        else:
            a = int(a)

        func = choices[choice]
        return func(a)
    return 'Invalid Choice'

# while True:
#     a = input('type [c, d, p, q]: ')
#     print(sound(a))




# create an empty dictionary
d = {}
# d2 = dict()

# add/update a value to the dictionary
key = 'cat'
value = 'meow'
d[key] = value
#d['cat'] = 'meow'
d['dog'] = 'woof'
d['pig'] = 'oink'

# check if key in dictionary
# if key in dictionary:
if 'cat' in d:
    print('"cat" in dictionary')

# get the value from a dictionary?
#print(d[key])
print(d['cat']) # 'meow'


# iterating (looping) through a dictionary
#for key in dictionary
for key in d:
    print(key, d[key])

# for key, value in d.items():
#     print(key, value)




# check if value in the dictionary?
for key in d:
    value = d[key]
    if value == 'oink':
        print('"oink" is a value in the dictionary. Its key is', key)

# if "oink" in d.values():
#     print('found "oink"')


shopping_cart = [
    {'name':'milk', 'price':2.38, 'discount':0.2},
    {'name':'candy', 'price':1.75, 'discount':0}
]

def subtotal(shopping_cart):
    total = 0
    for item in shopping_cart:
        price = item['price']
        discount = item['discount']


        d = price * discount
        total += price - d
    return total


def print_cart(shopping_cart):
    return


def find_item(shopping_cart, item):
    return


print(subtotal(shopping_cart))