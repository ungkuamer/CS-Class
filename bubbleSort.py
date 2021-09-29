myList = [27,19,36,42,16,89,21,16,55]
max = len(myList)-1

for i in range(max-1):
    for j in range(max):
        if myList[j] > myList[j+1]:
            temp = myList[j]
            myList[j] = myList[j+1]
            myList[j+1] = temp

print(myList)


