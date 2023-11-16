# functions = a block of code which is executed only when it is called

from unicodedata import name


'''def hello(name=input("What is your name?: ")):
    print("hello! " + name.capitalize() +
          " welcome to this python sandbox project")


hello()
'''


def hello(first_name, last_name, age):
    print("hello " + first_name+" "+last_name)
    print("You are " + str(age) + " years old")
    print("Have a nice day")


hello("Bro", "Code", 21)
