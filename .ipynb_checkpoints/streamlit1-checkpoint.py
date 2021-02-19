import streamlit as st


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
# ファイルをアップロードする機能

uploaded_file = st.file_uploader("Choose", type="jpeg")
if uploaded_file is not None:
    # ファイルがアップロードされたら、画像を表示させる。そのファイルを画像にして、img変数に入れる。
    img = Image.open(uploaded_file)
    st.image(img, caption="uploaded Image.", use_column_width=True)
