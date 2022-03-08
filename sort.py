def sort_list(list):
    i = 0
    j= i +1
    k = len(list)
    while i < k:
        while j < k:
            if list[j] > list[i]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
                i += 1
                j = i + 1
            else :
                i += 1
                j = i + 1
                break
    return list