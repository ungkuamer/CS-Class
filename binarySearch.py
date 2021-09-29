myList = [2,4,7,10,11,14,15,17,20]
highest = 9
lowest = 0
found = False

item = input('Please enter item to be found: ')
item = int(item)

while found == False and lowest <= highest:
    index = int((highest+lowest)/2)

    if item == myList[index]:
        found = True

    elif item > myList[index]:
        lowest = index + 1

    elif item < myList[index]:
        highest = index - 1

if found == True:
    print('Item Found')

else:
    print('Item not Found')




