students = {'Ahmad':69, 'Ali':42, 'John':77}

print(students.get('Ahmad'))
students['Susan'] = 86
students.pop('Susan')
print(students)

total, highest, = 0, 0
lowest = list(students.items())[0][1]


for i in students:
    total = total + students[i]
    
    if students[i] > highest:
        highest = students[i]

    if students[i] < lowest:
        lowest = students[i]

average = total/(len(students))
print('Average is: ', int(average))
print('Highest is: ', highest)
print('Lowest is: ', lowest)