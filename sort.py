def sort_list(list):
    i = 0
    j= i +1
    k = len(list)
    while i < k:
        j = 0
        while j < i:
            if list[i] < list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
                i += 1
                j = i + 1
            j += 1
    return list