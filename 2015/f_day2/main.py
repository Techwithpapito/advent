#formula 
#2*l*w + 2*w*h + 2*h*l  + the area of the smallest side
#example 
#2x3x4  =  2*6 + 2*12 + 2*8 = 52  + 6 = 58
#1x1x10 =  2*1 + 2*10 + 2*10 = 42 + 1 = 43

meters_square = 0
with open('data.txt',"r") as f:
    lines = f.readlines()
    for line in lines:
        equation = line.strip('\n').split('x')
        l = int(equation[0])
        w = int(equation[1])
        h = int(equation[2])
        ribbonFeet = (l*w*h) 
        ribbon = 2 * min(l+w, w+h, h+l)
    
        meters_square += (ribbonFeet + ribbon)


print(meters_square)