import hashlib


start = True
count=0
text="iwrupvqb"
while start:
    str2hash = f"{text}{count}"
    result = hashlib.md5(str2hash.encode())
    test = result.hexdigest()
    if test[0:6] == "000000":
        print("found")
        print(count)
        start = False
    else:
        count += 1