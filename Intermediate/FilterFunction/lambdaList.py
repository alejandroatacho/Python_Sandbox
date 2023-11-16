a = [1,2,3,4,5,6,7,8,9,10]
newList = list(map(lambda x: x+5,a))
newList2 = list(filter(lambda x: x%2==0, a));
result = str(newList);
result2 = str(newList2);
print(result +"<-- lambda 1, lambda2 --> "+ result2);