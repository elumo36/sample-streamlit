colors = ["赤","青","黄色","白"]

c = input("色を入力してください=>")
try:
    if colors.index(c) >= 0:
        print("入力されたものは、リストにあります。")
except:
        print(f"{c}は、リストにありません。")