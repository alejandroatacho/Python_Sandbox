# 5 Lambda Tutorial

def func(x):
    return x+5;

func2 = lambda x: x+5%5;
func3 = lambda x,y=5:x+y;

print(func(2));
print(func2(9));
print(func3(15));

