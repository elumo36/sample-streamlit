import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://scraping-for-beginner.herokuapp.com/ranking/"
res = requests.get(url)

# textは、中身を取得する。
# resu.text
#
# 以下のことをしないと、それは、たんなる文字列、HTMLではない。
#soup = BeautifulSoup(res.text, 'html.parser')
#
# 1つの観光地の情報を取ってくる。
##spots = soup.find_all("div", attrs={"class": "u_areaListRankingBox"})
#spots = soup.select(".u_areaListRankingBox")
#
#spot = spots[0]
# find_allに一度してみて、１つしかなければ、findに変えるといい。
#spot_name = spot.find("div", attrs={"class": "u_title"})
# 1観光地 1になる
# ここからいらない部分をとる。１
#spot_name.find('span', attrs={"class": "badge"}).extract()
#
# print(spot_name.text)改行が入る
##
# 観光地 1
##
#
#spot_name = spot_name.text.replace("\n", "")
# print(spot_name)
#
# 評点をとる。
# いったん、find_allでとってみる。
#spot_point = spot.find("div", attrs={"class": "u_rankBox"})
#point = spot_point.find("span", attrs={"class": "evaluateNumber"}).text
#point = float(point)
# print(point)
#
#category_items = spot.find("div", attrs={"class": "u_categoryTipsItem"})
# 複数あるので、リストの形で取得
#category_items = spot.find_all("dl")
#
#category_item = category_items[0]
#rank = float(category_item.span.text)
# print(rank)
# print(category_item.dt.text)
#
# 楽しさ：４．２みたいに辞書で取ってくる。
#details = {}
##category_item = category_items[0]
##rank = float(category_item.span.text)
##category = category_item.dt.text
##details[category] = rank
# print(details)
#
# それをfor文で回す。
# for category_item in category_items:
#    rank = float(category_item.span.text)
#    category = category_item.dt.text
#    details[category] = rank
# print(details)
#
# detailsは変数名として一部分なので、全体としてdatumにする
#
#datum = details
#datum["観光地名"] = spot_name
#datum["評点"] = point
# １つの観光地の欲しいデータを全て取ってくることができた。
# print(datum)

# ページすべての観光地のデータを取ってくる。for文で。
soup = BeautifulSoup(res.text, 'html.parser')

# 1つの観光地の情報を取ってくる。
#spots = soup.find_all("div", attrs={"class": "u_areaListRankingBox"})
spots = soup.select(".u_areaListRankingBox")
data = []
for spot in spots:

    spot_name = spot.find("div", attrs={"class": "u_title"})
    #spot_name.find('span', attrs={"class": "badge"}).extract()
    spot_name = spot_name.text.replace("\n", "")

    spot_point = spot.find("div", attrs={"class": "u_rankBox"})
    point = spot_point.find("span", attrs={"class": "evaluateNumber"}).text
    point = float(point)

    category_items = spot.find("div", attrs={"class": "u_categoryTipsItem"})
    # 複数あるので、リストの形で取得
    category_items = spot.find_all("dl")

    details = {}
    for category_item in category_items:
        rank = float(category_item.span.text)
        category = category_item.dt.text
        details[category] = rank
    datum = details
    datum["観光地名"] = spot_name
    datum["評点"] = point
    data.append(datum)
# print(data)

df = pd.DataFrame(data)
# print(df)

# カラムの順番を入れ替える
df = df[['観光地名', '評点', 'アクセス', '楽しさ', '人混みの多さ', '景色']]
# print(df.columns)
df.to_csv("観光地情報.csv", index=False)
