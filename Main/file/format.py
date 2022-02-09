'''animal = "cow"
item = "moon"
test = int(input("Write a number down: "))

print("The {} jumped over the {} about {} times".format(animal, item, test))
print("The {0} jumped over the {2} about {1} times".format(animal, item, test))'''
print("The {animal} jumped over the {item}".format(
    animal=input("Write an animal name: "), item=input("Name an item: ")))
