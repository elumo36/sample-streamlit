sosu = [2]
for n in range(3,501,2):
    for p in sosu:
        key = True
        if n % p == 0:
            key = False
            break
    if key == True:
        sosu.append(n)
print(sosu)

