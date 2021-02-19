import random

ave = []
count = 0
ok = 0

while True:
    num1 = random.choice(range(1,200))
    num2 = random.choice(range(1,200))
    if num1 == num2:
        count += 1
        ok += 1
        ave.append(count)
        if ok >= 5:
            averag = sum(ave)/ len(ave)
            print(ave)
            print(averag)
            break
        else:
            continue
    else:
        count += 1


