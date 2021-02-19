num = input("数を入力してね。")
for n in range(2, int(num)):
    key = True
    if int(num) % n == 0:
        key = False
        break
if key == True:
    print(num + "は素数です")
else:
    print(num + "は素数ではない")

