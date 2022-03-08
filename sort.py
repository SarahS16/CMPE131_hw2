def sort_list(list):
    i = 0
    j= i +1
    k = len(list)
    while i < k:
        i += 1
        j += 1
        while j < k:
            if list[j] > list[i]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            else :
                break
    return list