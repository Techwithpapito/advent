floor = 0
position = 1
with open('data.txt',"r") as f:
    words = f.readline()
    for word in words:
        if word == "(":
            floor += 1
            position +=1
        if word == ")":
            floor -= 1
            position += 1
        if floor < 0:
            print(position)
            break
    print(position)