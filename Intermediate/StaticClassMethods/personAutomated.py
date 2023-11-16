class Person(object):
    population = 50

    def __init__(self):
        self.name = input("What is your name? ")
        self.age = int(input("What is your age? "))

    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod
    def is_adult(age):
        return age >= 18

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating a new instance of the Person class, inputting name and age
new_person = Person()

# Displaying information about the person
new_person.display()

# Accessing class methods
print(Person.get_population())  # Output: 50

# Using a static method to check if a person is an adult
if Person.is_adult(new_person.age):
    print("You can apply for driving classes.")
else:
    print("You are not considered an adult for driving.")
