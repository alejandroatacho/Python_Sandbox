'''item_log = input("Enter a list of items: ")

list_log = item_log.split(',')'''

i = 0
item_holder = []
end_line = 5
while i != end_line:
    item_log = input("Enter a list of items: ")
    list_log = item_log.split(',')
    list_log = item_holder + list_log
    print(item_log)
    i += 1

    if i == end_line:
        print("you have reached the end of the list")
        print(list_log)
        break
    else:
        print("you have not reached the end of the list")
        'continue'
