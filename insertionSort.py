myList = [53,21,60,18,42,19]
no_item = len(myList)

for i in range(no_item):
    item_insert = myList[i]
    prev = i-1

    while (myList[prev]) > item_insert and (prev > -1):
        myList[prev+1] = myList[prev]
        prev = prev - 1

    myList[prev + 1] = item_insert

print(myList)
