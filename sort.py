def sort_list(list):
    k = len(list)

    while i < (k-1):
        while 0 < j < (k-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
            j += 1
        i += 1

    return list