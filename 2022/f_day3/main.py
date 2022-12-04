letterPrice = {"a": 1,"b":2,"c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26,
 "A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52}

total = 0
listLines = []
old_position = 0
new_position = 2
with open("data.txt",'r') as f:
    lines = f.readlines()
    for line in lines:
        listLines.append(line.strip("\n"))

    totalLength = len(listLines)
    while new_position < totalLength:
        a=list(set(listLines[old_position])&set(listLines[old_position+1])&set(listLines[new_position]))
        for i in a:
            total += letterPrice[i]
        old_position = new_position + 1
        new_position = old_position + 2
        

    # for line in lines:
    #     x = len(line)
    #     string1 = slice(0,x//2)
    #     string2 = slice(x//2,x)
    #     print(line[string1],line[string2])
    #     a=list(set(line[string1])&set(line[string2]))
    #     for i in a:
    #         total += letterPrice[i]

print(total)