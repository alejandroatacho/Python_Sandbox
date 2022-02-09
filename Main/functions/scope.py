'''scope= the region that a variable is recognized
    `       a variable is only available from inside the region it is created.
            a globalandlocally scoped versions of a variable can be created'''

name = "Bro code"  # global scope


def display_name():
    name = "code"  # local scope (only availble within the function)
    print(name)


display_name()
print(name)
