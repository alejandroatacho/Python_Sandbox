'''keyword arguments = argument preceded by an indentifier when we pass them to a function
                        the order of the argumens doesn't matter, un like positional arguments.
                        python knows the names of the argument that our functions recieved.'''


def hello(first, middle, last):
    print("Hello " + first+" " + middle+" "+last)


hello(last="code", middle="dude", first="bro")
