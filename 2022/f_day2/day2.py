# Rock defeats Scissors,  A,X: C,Z
# Scissors defeats Paper, C,Z:B,Y
# and Paper defeats Rock. B,Y:A,X

#oponent
# A for Rock, # X for Rock,
# B for Paper, #  Y for Paper, 
# and C for Scissors. # and Z for Scissors.

#me
# (1 for Rock X,
#  2 for Paper Y,
#  and 3 for Scissors Z

# + the outcome of the round (0 if you lost, 
# 3 if the round was a draw, 
# and 6 if you won).

#[0] is oponent   [2] is me
total_points = 0

# WINNING = {"B Z":9,"C X": 7,"A Y": 8,"C Z":6,"B Y":5,"A X":4}
# LETTERS = {"Z":3,"Y":2,"X":1}
# X = losing
# Y = draw
# Z = win
WINNINGCom = {"A": 8,"B":9,"C":7}
LOSINGCom = {"A":3,"B":1,"C":2}
DRAWCom = {"A":4,"B":5,"C":6}


with open('data.txt',"r") as f:
    lines = f.readlines()
    for line in lines:
        line = f"{line[0]} {line[2]}"
        if line[2] == "X":
         #losing
            total_points += LOSINGCom[line[0]]
        if line[2] == "Y":
            #draw
            total_points += DRAWCom[line[0]]
        if line[2] == "Z":
            #win
            total_points += WINNINGCom[line[0]]

        

print(total_points)




