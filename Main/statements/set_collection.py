# set = collection which is unordered, unindexed. no duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.update(dishes) # merge 2 tables
#dinner_table = utensils.union(dishes)
print(utensils.difference(dishes))
print(utensils.intersection(dishes))

'''for x in utensils:
    print(x, end=" ")
    print()
    print(dinner_table, end=" ")
'''
