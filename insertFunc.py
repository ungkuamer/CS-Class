def insertionSort(link_list):
    no_item = len(link_list)

    for i in range(no_item):
        item_insert = link_list[i]
        prev = i-1

        while (link_list[prev]) > item_insert and (prev > -1):
            link_list[prev+1] = link_list[prev]
            prev = prev - 1

        link_list[prev + 1] = item_insert

    return(link_list)

def bubbleSort(link_list):
    max = len(link_list)-1

    for i in range(max):
        for j in range(max):
            if link_list[j] > link_list[j+1]:
                temp = link_list[j]
                link_list[j] = link_list[j+1]
                link_list[j+1] = temp

    return(link_list)



