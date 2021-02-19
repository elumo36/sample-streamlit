# ファイル名をturtle.pyにすると、importせず、そのファイルを読み込んでしまうので注意。
import turtle
# システム関連の関数が入っているモジュール
import sys


def draw_circle(x, y):
    my_turtle.penup()
    my_turtle.goto(x, y - radius)
    my_turtle.pendown()
    my_turtle.circle(radius)


def draw_line(x, y):
    my_turtle.ondrag(None)
    my_turtle.setheading(my_turtle.towards(x, y))
    my_turtle.goto(x, y)
    my_turtle.ondrag(draw_line)


my_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.setup(800, 800)

screen.title("タートル")
# タートルの形を決める
my_turtle.shape("turtle")
my_turtle.pensize(4)
my_turtle.color("blue")

# 円の半径
radius = 100

# screen.onscreenclick(draw_circle)
my_turtle.ondrag(draw_line)


# タートルを動かす
# my_turtle.forward(150)
# my_turtle.left(90)
# my_turtle.forward(150)
# my_turtle.right(90)

#c = input("1:赤、2:緑：")
# if c == "1":
#    my_turtle.color("red")
# elif c == "2":
#    my_turtle.color("green")
# else:
#    print("１か２を入力してください。")
#    sys.exit()
#
# my_turtle.circle(100)


screen.mainloop()


# exitonclick()  マウスをクリックしたときに、終了する。
