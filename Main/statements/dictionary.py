'''dictionary = a changeable, unordered collection of unique key: value pairs,
   it is fast because they use hasing and allow us to acess a value quickly'''
capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})
capitals.pop('China')  # delete value
# capitals.clear() #remove every value

print(capitals['Russia'])
print(capitals.get('Germany'))
print(capitals.keys())  # value
print(capitals.values())  # inner value
print(capitals.items())  # print each value and there inner

for key, value in capitals.items():
    print(key, value, end=" ")
