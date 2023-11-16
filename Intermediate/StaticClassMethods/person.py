inputName = input("What is your name? ")
inputAge = int(input("What is your age? "))

class Person(object):
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod
    def is_adult(age):
        return age >= 18

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating a new instance of the Person class
new_person = Person(inputName, inputAge)

# Displaying information about the person
new_person.display()

# Accessing class methods
print(Person.get_population())  # Output: 50

# Using a static method to check if a person is an adult
print(Person.is_adult(18))  # Output: False

if new_person.age >= 18:
    print("You can apply for driving classes.")
else:
    print("The function 'is_adult' does not consider you an adult for driving.")
