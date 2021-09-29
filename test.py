# declare myLinkedList array[0:11] of integer
# declare myLinkedListPointers array[0:11] of integer
# declare startPointer : integer
# declare heapStartPointer : integer
# declare index : integer
heapStartPointer = 0
myLinkedListPointers = [0]*12
startPointer = -1 
for i in range(0, 11):
    myLinkedListPointers[i] = i + 1

myLinkedListPointers[11] = -1