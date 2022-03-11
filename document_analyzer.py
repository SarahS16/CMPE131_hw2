
words = open("/home/sarah/Desktop/CMPE131/Hw2/document.txt","r")
words = words.read().strip()
words = words.lower()
words = words.split()
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



for keys in list(sorted_counter.keys()):
    print(keys, ":", sorted_counter[keys])


