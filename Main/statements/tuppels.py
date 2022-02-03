# tupple collection which is ordered and unchangable, used to group togheter related data
student = ("bro", 21, "male")

print(student.count("bro"))
print(student.index("male"))

for x in student:
    print(x, end=" ")
print()
if "bro" in student:
    print("He is here")
