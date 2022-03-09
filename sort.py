def sort_list(list):
    k = len(list)
    i = 0
    while i < (k):
        j = 0
        while 0 < j < (k-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            j += 1
        i += 1

    return list