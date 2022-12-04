import re

def is_nice(string):
    return (
        re.search(r'(..).*\1', string) and 
        re.search(r"(.).\1", string)
    )


count = 0

with open('data.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        if is_nice(line.strip('\n')):
            count += 1

print(count)