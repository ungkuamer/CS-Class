myList = [4,2,8,17,9,3,7,12,34,21]
found = False

item = input('Please enter item: ')
item = int(item)

for i in range(len(myList)):
    if myList[i] == item:
        found = True
        index = i

if found:
    print('Item found at location: ' + str(index))

else:
    print('Item not found')


