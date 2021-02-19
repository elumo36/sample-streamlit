import turtle
import math
import random
import datetime


def tleft():
    # 左に回転
    my_turtle.left(10)


def tright():
    # 右に回転
    my_turtle.right(10)


def is_hit(target, turtle):
    # タートルとターゲットの衝突判定
    # pow(x,y)x元の数のy乗を返す、戻り値はfloat
    # sqrtは、平方根の値を返す
    diff = math.sqrt(math.pow(target.xcor()-turtle.xcor(), 2)
                     + math.pow(target.ycor()-turtle.ycor(), 2))
    # 距離が40px以下になれば当たり判定
    return True if diff < 40 else False


def game():
    global count
    # tiltは、タートルを引数分角度を傾けるメソッド。
    # この２つを何度も１０msごと繰り返しているので、動きながら回転している
    if math.fabs(my_turtle.xcor()) >= X_LIMIT:
        angle = 180 - my_turtle.heading()
        my_turtle.setheading(angle)
        print(angle)
    if my_turtle.ycor() >= Y_LIMIT:
        angle = 360 - my_turtle.heading()
        my_turtle.setheading(angle)

        # 変数dtepだけ移動させる
    my_turtle.forward(step)

    # ターゲットを移動させる
    for t in targets:
        t.forward(random.randrange(10))
        # ターゲットの回転
        t.tilt(3)
        if math.fabs(t.xcor()) > X_LIMIT:
            t.right(180)
            t.forward(10)
        if is_hit(t, my_turtle):
            # ヒットしたターゲッ戸を灰色にしてtargetsから取り除く
            t.color("#EEEEEE")
            targets.remove(t)
            r_text.clear()
            r_text.write(
                f"残りターゲット：{len(targets)}",
                font=("helvetica", 24)
            )
    # 経過時間を計算する
    now = datetime.datetime.now()
    etime = now - stime

    # ターゲットが残っていれば経過時間を更新
    if len(targets) > 0:
        count += 1
        if count % 5 == 0:
            # sec = 前回との差（秒の部分）+  前回との差（マイクロ秒の部分）1000000で割って秒と合わせている。
            sec = etime.seconds + etime.microseconds / 1000000
            time_text.clear()
            # 小数点第一位まで表示
            time_text.write(f"経過時間：{sec:.1f}秒", font=("helvetica", 24))
    else:
        time_text.goto(-250, 0)
        time_text.write("ミッション完了", font=("helvetica", 60))
        screen.update()
        return

    # タートルが下の壁にぶつかったらゲームオーバー
    # タートルのY座標が-400以下のときゲームオーバー
    if my_turtle.ycor() < -Y_LIMIT:
        screen.tracer(1)
        my_turtle.color("red")
        # タートルを震わせる
        for _ in range(10):
            my_turtle.right(15)
            my_turtle.left(15)
        time_text.goto(-280, 0)
        time_text.write(
            "ゲームオーバー", font=("helvetica", 60)
        )
    else:
        # 画面を強制的にアップデート
        screen.update()
        screen.ontimer(game, 10)


# 画面の作成、設定
screen = turtle.Screen()
screen.setup(900, 900)
screen.title("ゲーム")

# タートルのインスタンスを生成
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("orange")
my_turtle.shapesize(3)
my_turtle.penup()

# 全てを違う色に指定したい場合
# colors = ["blue", "green", "black", "purple", "pink", "yellow", "orange"]
# random.shuffle(colors)
# pop()メソッドは、リストから最後の要素を削除して、その値を戻すメソッド。
# target.color(colors.pop())

# ターゲットを格納するリスト
targets = []
# ターゲット数
num_of_targets = 6
colors = ["blue", "green", "black", "purple", "pink", "yellow", "orange"]

# ターゲットを描く。四角のやつ。
for y in range(num_of_targets):
    target = turtle.Turtle()
    # まずは、ペンを上げておく
    target.penup()
    # ランダムに色を決める
    target.color(random.choice(colors))
    # 形は、四角に大きさも決める
    target.shape("square")
    target.shapesize(2)
    # ターゲッとのX座標を設定する。引数が位置
    target.setx(-400 + random.randrange(4)*100)
    # ターゲッとのY座標を設定する。引数が位置
    target.sety(y * 100 - 300)
    targets.append(target)


# キーイベント
# キーの監視を有効化
screen.listen()
screen.onkey(tleft, "Left")
screen.onkey(tright, "Right")
# トレーサーをオフにする
screen.tracer(0)

# 残りターゲット表示テキスト用
r_text = turtle.Turtle()
r_text.penup()
r_text.hideturtle()
r_text.goto(-380, -350)
r_text.write(f"残りターゲット：{len(targets)}",
             font=("helvetica", 24))


# 経過時間表示テキスト用
time_text = turtle.Turtle()
time_text.penup()
time_text.hideturtle()
time_text.goto(0, -350)
# 経過時間
etime = 0

# 境界,壁になる位置を指定する
X_LIMIT = 400
Y_LIMIT = 400

# スタート時間
stime = datetime.datetime.now()

# タートルのループマイの移動時間
step = 3

# タートルの角度
angle = 40


# turtleには、leftメソッドで、引数分回転させることができる。
# つまり、北東に向かう。
my_turtle.left(angle)

# game()関数が何回呼ばれたか。（経過時間表示用）
count = 0

# ゲームの開始
game()
screen.mainloop()
