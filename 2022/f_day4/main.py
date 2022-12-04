   
count = 0
with open("data.txt",'r') as f:
    lines = f.readlines()

    for line in lines:
        splitedLine = line.strip('\n').split(",")
        leftRange = splitedLine[0]
        rightRange = splitedLine[1]
        splitLeftRange = leftRange.split("-")
        splitRightRange = rightRange.split("-")
        minLeft = int(splitLeftRange[0])
        maxLeft = int(splitLeftRange[1])
        minRight = int(splitRightRange[0])
        maxRight = int(splitRightRange[1])
        listaLeft = [x for x in range(minLeft,maxLeft+1)]
        listaRight = [x for x in range(minRight,maxRight+1)]
        a_set = set(listaLeft)
        b_set = set(listaRight)
        if (a_set & b_set):
            count += 1

        

print(count)

