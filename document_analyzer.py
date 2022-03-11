


with open("/home/sarah/Desktop/CMPE131/Hw2/document.txt", "r") as analyze:
    words = analyze.read().split()




counter = dict()
for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1


sorted_val = sorted(counter.values(), reverse = True)
sorted_counter = {}

for i in sorted_val:
    for j in counter.keys():
        if counter[j] == i:
            sorted_counter[j] = counter[j]
            break

#print(list(sorted_counter.items())[0:5])
