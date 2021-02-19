import random
import re
a = [random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9)]
perfect = False
isok = False
while perfect == False:
    while isok == False:
      b = input("数を入力してね")
      if not re.match(r"^\d\d\d\d$", b):
        print ("4桁の数を入力してください。")
      else:
        isok = True


    hit = 0
    brow = 0
    for i in range(4):
        if a[i] == int(b[i]):
            hit += 1
        else:
            for n in range(4):
                if a[i] == int(b[n]):
                  brow += 1
                  break
    if hit == 4:
        perfect = True
    else:
        print("ヒットは:" + str(hit) )
        print("ブローは:" + str(brow) )
        #print("hitは" + hit + "で、ブローは、"+ brow + "です。")
        isok = False
        print("もう一度、入力しなおしてください。")
else:
    print("perfectです。")


    