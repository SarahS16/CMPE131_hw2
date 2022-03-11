
words = open("/home/sarah/Desktop/CMPE131/Hw2/document.txt","r")
words = words.read().strip()
words = words.split()
words.sort()
counter = dict()
for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

sorted_val = dict(sorted(counter.items(), key = lambda x:x[1], reverse = True))


for keys in list(sorted_val.keys())[0:5]:
    print(keys, ":", sorted_val[keys])


