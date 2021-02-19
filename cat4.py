# 画像の取得方法
import requests
from bs4 import BeautifulSoup
# 画像の保存に関してのものPillow(PIL)による画像処理,
# リサイズやトリミングなどの基本的な処理を行いたい場合
from PIL import Image
# ファイルの入出力などを行うときのライブラリ
import io

#url = "https://scraping-for-beginner.herokuapp.com/image"
#res = requests.get(url)
# htmlの構造に変える。resの中身を
#soup = BeautifulSoup(res.text, "html.parser")
#img_tag = soup.find("img")
# print(img_tag)
# これで、imgタグのsrcを取ってこれる。
# https://scraping-for-beginner.herokuapp.com/image/  srcの内容をくっつける！

# ()ではないので注意。
# print(img_tag["src"])

# 画像のurlを作成
#root_url = "https://scraping-for-beginner.herokuapp.com"
#img_url = root_url + img_tag["src"]
# print(img_url)

# ただ、requests.get(img_url)をするだけでは、みられないバイナリデータ。形式を変える。io
# それを画像にするわけ。
#img = Image.open(io.BytesIO(requests.get(img_url).content))
# それを保存する
# img.save("img/sample.jpg")

# すべての画像を保存するので、find_allにする
url = "https://scraping-for-beginner.herokuapp.com/image"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# find_all
img_tags = soup.find_all("img")

root_url = "https://scraping-for-beginner.herokuapp.com"
#num = 1
# for img_tag in img_tags:
#    img_url = root_url + img_tag["src"]
#    img = Image.open(io.BytesIO(requests.get(img_url).content))
#    img.save(f"img/{num}.jpg")
#    num += 1

for i, img_tag in enumerate(img_tags):
    img_url = root_url + img_tag["src"]
    img = Image.open(io.BytesIO(requests.get(img_url).content))
    img.save(f"img/{i}.jpg")
