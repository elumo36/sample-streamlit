# coding:utf-8
import tkinter as tk
import tkinter.messagebox as tmsg
import random
#正規表現のモジュール
import re

#ボタンが押されたときの処理
def ButtonClick():
    #テキスト入力欄に入力された文字列を取得
    b = editbox1.get()

    #入力された数字を表示したい場合
    #tmsg.showinfo("入力されたテキスト", b )


    perfect = False
    isok = False
    while perfect == False:
        while isok == False:
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
            #終了させる。
            root.destroy()
        else:
            #print("ヒットは:" + str(hit) )
            #print("ブローは:" + str(brow) )
            #print("hitは" + hit + "で、ブローは、"+ brow + "です。")
            #isok = False
            #print("もう一度、入力しなおしてください。")
            #tk.ENDは、つけることで、末尾に挿入されるようになる。
            rirekibox.insert(tk.END, b + "  /H:" + str(hit)+ " B:"+ str(brow)+ "\n")

    else:
        print("perfectです。")



#メインプログラム
#あらかじめ、ランダムな４つの数を作成しておく。
a = [random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9)]

root = tk.Tk()
root.geometry("600x400")
root.title("数当てゲーム")

#履歴表示のテキストボックスを作る
rirekibox = tk.Text(root,font=("Helvetica",14))
rirekibox.place(x=400,y=0,width=200, height=400)

root.Label(root, text="数を入力してください。",font=("",14))
Label.place(x=20,y=30)



editbox1 = tk.Entry(width=4,font=("",14))
editbox1.place(x=120,y=30)

button1 = tk.button(root ,text="チェック",font=("",14), command=ButtonClick )
button1.place(x=220,y=60)


root.mainloop()
