dictionary = {}

with open('data.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        splitedLine = line.strip('\n').split(' ')
        if splitedLine[0] == "turn":
            action = f"{splitedLine[0]} {splitedLine[1]}"
            beginningCordinate = splitedLine[2]
        else:
            action = splitedLine[0]
            beginningCordinate = splitedLine[1]

        endCordinate = splitedLine[-1]
        
        beginningCordinate = beginningCordinate.split(',')
        endCordinate = endCordinate.split(',')
        startX = int(beginningCordinate[0])
        endX = int(endCordinate[0])
        startY = int(beginningCordinate[1])
        endY = int(endCordinate[1])

        for x in range(startX,endX+1):
            for y in range(startY,endY+1):
                if (x,y) not in dictionary:
                    dictionary[(x,y)] = 0

                if action == "turn on":
                    dictionary[(x,y)] += 1
                if action == "turn off":
                    if (dictionary[(x,y)] - 1) < 0:
                         dictionary[(x,y)] = 0
                    else:
                        dictionary[(x,y)] -= 1 
                if action == "toggle":
                    dictionary[(x,y)] += 2
                     


count = 0
for coordinate, stat in dictionary.items():
    count += stat

print(count)