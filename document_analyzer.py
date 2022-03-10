analyze = open("document.txt", 'r')
most_f = ""
second_f = ""
third_f = ""
fourth_f = ""
fifth_f = ""
frequent_1 = 0
frequent_2 = 0
frequent_3 = 0
frequent_4 = 0
frequent_5 = 0
word_list = []

words = analyze.split()
words.sort()
k = len(words)
for n in words:
    word_list.append(n)

for i in range(0,k):
    count = 1
    for j in range(i+1,k):
        if(word_list[i] == word_list[j]):
            count += 1

    if(count > frequent_1):
        frequent_1 = count
        most_f = word_list[i]
    if(frequent_1 > count > frequent_2):
        frequent_2 = count
        second_f = word_list[i]
    if(frequent_2 > count > frequent_3):
        frequent_3 = count
        third_f = word_list[i]
    if(frequent_3 > count > frequent_4):
        frequent_4 = count
        fourth_f = word_list[i]
    if(frequent_4 > count > frequent_5):
        frequent_5 = count
        fifth_f = word_list[i]

print(most_f, ":", frequent_1 )
print(second_f, ":", frequent_2 )
print(third_f, ":", frequent_3 )
print(fourth_f, ":", frequent_4 )
print(fifth_f, ":", frequent_5 )






    
    


#algorithm(?): read txt file with each word placed into a list: from that list each time adds plus 1 to word counter or moves word to the front? then returns the list of 5 with the word count
