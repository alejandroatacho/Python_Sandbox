#3 map function

li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x;

newList = [];
for i in li:
    result = func(i);
    result2 = i;
    print(f"{result2} the power of that answer is: {result}")
    # i += 1;
