from curses.ascii import islower
# broke the whole operator

name = "bro code"
y = 0
holder = ()
num = 0
for c in name:
    y += 1
print(y)
holder = y

while holder >= 0:
    if (name[num], islower()):
        name = name.capitalize()
print(name)
num += 1

'''if(name[0].islower()):
    name = name.capitalize()

print(name)
'''
