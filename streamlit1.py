# streamlit run streamlit1.py  で確認できる。command+R でリロード
import streamlit as st
# APIを叩くためのリクエストをするFaceAPIに
import requests
from PIL import Image
from PIL import ImageDraw
# データの入出力をするときなどに使う
import io

import pandas as pd
import numpy as np
# 画像の読み込み
from PIL import Image
# Pythonでグラフを作成するためには、「matplotlib」というライブラリを使用するのが一般的
#import matplotlib.pyplot as plt

st.title("My 1st App")
# streamlit run streamlit1.py  で確認できる。command+R でリロード

st.write("データフレーム")
# 表を表示
st.write(
    pd.DataFrame({
        "1st column": [1, 2, 3, 4],
        "2nd column": [10, 20, 30, 40]
    })
)

# 棒グラフ
#left = np.array([1, 2, 3, 4, 5])
#height = np.array([100, 200, 300, 400, 500])
#plt.bar(left, height)
# plt.show()

# マジックコマンド"""
# マークダウンで書く。#とかを使う。
"""
# 見出し１の書き方。
## マジックコマンドでの見出し２の書き方
ここは、普通の文字になる。 

"""

# チェックボックスによってインタラクティブにできる
if st.checkbox("Show DataFrame"):
    # チャート20行３列で正規分布からランダムの数を取ってくる
    chart_df = pd.DataFrame(
        np.random.randn(20, 3),
        columns={"a", "b", "c"}  # ３列あるので
    )

    # チャートを書く場合。インタラクティブ
    st.line_chart(chart_df)


# 画像のアプリ
st.title("顔認識アプリ")


SUBSCRIPTION_KEY = ""
assert SUBSCRIPTION_KEY
face_api_url = "https://tori-sample.cognitiveservices.azure.com/face/v1.0/detect"

# ファイルをアップロードする機能
uploaded_file = st.file_uploader("Choose", type="jpeg")
if uploaded_file is not None:
    # ファイルがアップロードされたら、画像を表示させる。そのファイルを画像にして、img変数に入れる。
    img = Image.open(uploaded_file)
    # 画像を読み込むpillow
    #img = Image.open("s4.jpg")

    # APIに送っても顔を検出してくれないので、バイナリデータにする。
    # with open("s4.jpg","rb") as f:
    #    binary_img = f.read()       #readメソッドで、バイナリデータに変換する。

    # ここで、バイナリデータを取得
    with io.BytesIO() as output:
        img.save(output, format="JPEG")
        binary_img = output.getvalue()  # バイナリデータを取得
    # io.BytesIO()
    # face-apiの決まりのようなもの。face_api_urlが、直接URLになっているから。画像をおくりますよ！
    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}
    params = {
        # 'detectionModel':'detection_02'
        'returnFaceId': 'true',
        # 顔の位置情報以外に取ってくる。
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,makeup,hair,noise'
    }
    # 受け取った情報を、resに格納
    res = requests.post(face_api_url, params=params,
                        headers=headers, data=binary_img)  # json={"url":image_url})

    # 複数人いる場合を想定して、for文で回す。json形式にする
    results = res.json()

    for result in results:
        # 顔の位置を特定Face rectangle 位置情報。顔が１つだから[0]
        rect = result["faceRectangle"]

        gen = result["faceAttributes"]["gender"]
        #gen = '男' if gen == "male" else "女"
        # if  gen == "male":
        #    gen = '男'
        # else:
        #    gen = '女'
        age = str(result["faceAttributes"]["age"])
        #text = f"{gen}・{age}"
        # 線を描くための準備（なにに対して線を描くのか）（引数に指定）
        draw = ImageDraw.Draw(img)
        print(gen)
        # print(age)
        draw.rectangle([(rect['left'], rect['top']), (rect['left']+rect['width'], rect['top']+rect['height'])],
                       fill=None, outline="green", width=5)
        draw.text((rect['left'], rect['top']-15), gen +
                  age, fill='yellow', align='center')

        # streamlitで表示する。
        st.image(img, caption="uploaded Image.", use_column_width=True)
        # img

# github上にアップロード
# リポジトリ作成
# git init
# git remote add origin https://github.com/elumo36/sample-streamlit.git
# requirements.txtに標準ライブラリ以外の使用ライブラリを書く。
# git add .
# git commit -m "deployなど"
# git push origin master

# strealitシェアリング
