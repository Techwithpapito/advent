
#coordinate
# x = horizontal y = vertical
# north (^), south (v), east (>), or west (<)
coordinateDic = {}
coordinateDic[(0,0)] = 1
santaX,santaY = 0,0
roboX,roboY = 0,0
lista = [(roboX,roboY),(santaX,santaY)]



with open('data.txt','r') as f:
    letters = f.readline().strip(" ")
    for turn , letter in enumerate(letters.strip("\n"),start=1):
        turn = (turn % 2)
        #santa = 1
        #robot = 0
       
        
        north = lista[turn][1] + 1
        south = lista[turn][1] - 1
        east = lista[turn][0] + 1
        west = lista[turn][0] - 1
        
        if letter == "^":
            listTuple = list(lista[turn])
            listTuple[1] = north
            lista[turn] = tuple(listTuple)

        if letter == "v":
            listTuple = list(lista[turn])
            listTuple[1] = south  
            lista[turn] = tuple(listTuple)
          
        if letter == ">":
           listTuple = list(lista[turn])
           listTuple[0] = east  
           lista[turn] = tuple(listTuple)
        if letter == "<":
            listTuple = list(lista[turn])
            listTuple[0] =  west  
            lista[turn] = tuple(listTuple)
       

        if letter != " ":
            if not lista[turn] in coordinateDic:
                coordinateDic[lista[turn]] = 1
            else:
                coordinateDic[lista[turn]] += 1



count = 0
for coordinate, value in coordinateDic.items():
    if value >= 1 :
        count += 1

print(count)


