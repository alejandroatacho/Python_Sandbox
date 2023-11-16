from cgitb import text

text = "Hello World\nThis is some text\nHave a good one:\n"
apple = "Have a nice day! See ya "
# with open("main//file//placeholder//magic.txt", "w") as file:
#    file.write(text)
with open("main//file//placeholder//magic.txt", "a") as file:
    file.write(apple)
# doesn't overwrite but adds more ("a") causes it
