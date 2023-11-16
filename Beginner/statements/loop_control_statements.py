'''while True:
    name = input("enter your name: ")
    if name != "":
        break
print(name + " is your name!")'''

'''phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")'''

for i in range(1, 21):
    if i == 13:
        pass  # skip 13
    else:
        print(i)
