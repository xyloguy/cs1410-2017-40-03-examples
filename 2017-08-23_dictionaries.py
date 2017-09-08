d = {'value':'hi'}
empty_dict = {}

# set a value
d['key'] = 'value'

# update a value
d['key'] = 'hello, world'

print(d)
print(d['key'])

# check if item is in dictionary
if 'key' in d:
    print(d['key'])
else:
    print('"key" not in dictionary')

# loop for number of items
for i in range(5):
    print (i)

# loop over list
l = [1,2,3]
l[2] = 4
for item in l:
    print (item)

# loop over string
s = 'abc'
for char in s:
    print (char)

# loop over dictionary
for key in d:
    value = d[key]
    if value == "hi":
        print ('the value "hi" is there')

# loop over tuple
t = (1,2,3,4,5,6,7)
point = (1,2)
t[2] = 4
for item in t:
    print (item)




