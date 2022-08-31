# name = input("what is your name?: ")
# age = int(input("How old are you?: "))
# height = float(input("How tall are you?(cm): "))

# print("Hello " + name)
# print("You are "+str(age)+" years old")
# print("You are "+str(height)+" cm tall")

from pynput.keyboard import Key, Listener

key = []


while key != Key.esc:
    answer = input("Write your reply here: ")
    print(answer + "\n" + "\n Write your reply here: ")
    answer = input()
    if key == Key.esc:
        break
