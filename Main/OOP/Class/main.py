from classess import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "Red")
# print(car_1.make)

print("This "+car_1.model + " has "+str(car_1.wheels) + " wheels")
car_1.drive()
