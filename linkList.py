# DECLARE link_list ARRAY[0:11] OF INTEGER
# DECLARE link_list_pointer ARRAY[0:11] OF INTEGER
# DECLARE START_POINTER : INTEGER
# DECLARE HEAP_POINTER : INTEGER
# DECLARE index : INTEGER

# test data : lower bound, upper bound, in between  

import insertFunc # import function from other file

# initialisation
HEAP_POINTER = 0
START_POINTER = -1
NULL_POINTER = -1
link_list = []
link_list_pointer = []
num = 0

# populating list with value
for index in range(12):
    if num != -1:
        num = int(input('Enter number: '))
    if num != -1:
        link_list.append(num)

    link_list_pointer.append(index+1)
    HEAP_POINTER = HEAP_POINTER + 1

link_list_pointer[11] = -1

# sorting algorithm choice
algo_choice = int(input('Please choose algorithm (1: insertion sort, 2: bubble sort) -->  '))

if algo_choice == 1:
    final = insertFunc.insertionSort(link_list)
else:
    final = insertFunc.bubbleSort(link_list)

# insert new item into list


# output
print('link list:', final)
print('heap pointer:', HEAP_POINTER)
print('start pointer:', START_POINTER)
print('link list pointer:', link_list_pointer)






