max_points = 0
user_max = 0
user = 1
counter = 0
dictionary = {}
import operator


with open('data.txt',"r") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip():
            counter = counter + int(line)
        else:
            dictionary[user] = counter
            user = user + 1
            counter = 0

sorted_d = dict( sorted(dictionary.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)

list = []
count = 0
for i in sorted_d:
    if count < 3:
        count += 1
        print(sorted_d[i])
        list.append(sorted_d[i])
    else:
        break
final = sum(list)

print(final)



