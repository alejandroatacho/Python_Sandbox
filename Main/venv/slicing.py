# slicing = create a substring by extracting elements from another string
# indexing []or slice()
# [start:stop:step]

name = "Bro Code"
#first_name = name[0]
first_name = name[:3]
last_name = name[4:8]
funky_name = name[0:8:2]  # funky_name = name[::2] also possible
reversed_name = name[::-1]
website = "http://google.com"
slice = slice(7, -4)
#x = len(name)
x = int(len(name))
y = x
'''
 while y >= 0:
   print(name[y])
   y = y - 1
'''
# print(y)
print(len(name))
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name.lower())
print(website[slice])
