# 必要なライブラリ requests BeautifulSoup4
import requests
from bs4 import BeautifulSoup

URL = "https://scraping-for-beginner.herokuapp.com/udemy"
res = requests.get(URL)
# res.text
# htmlをstr型ではなく、html構造にする。
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.prettify())  インデントを整えて表示してみる。
# pタグ要素を全て取ってきてそのインデックス[1]を表示する。
# print(soup.find_all("p")[1])

# 最初のpタグを取ってくる  find.p
# find.p.text  <p>タグの中のテキスト部分を取ってくる

# [<p class="subscribers">受講生の数：10860</p>]を取ってくる。
# "p"の中でもclassの条件を追加する。
# 注意は、allは、リスト形式で取ってくるので、その中で[2]インデを指定する必要あり。
subsc = soup.find_all("p", attrs={"class": "subscribers"})[0]
text = subsc.text

# でも、これは、<class 'str'>
# print(type(text))
# print(text)    受講生の数：10860

n_subscribers = int(text.split("：")[1])  # 「：」と「:]注意
print(n_subscribers)

# cssのセレクタで取得することができる。
soup.select('.subscribers').text
# リスト形式ではない１つ指定の取得方法。
soup.select_one('.subscribers').text

# find_all("要素", attrs={"class": "subscribers"})[インデックス番号]
# そして、それを.textで、HTML構造にする


# soup.select_all('.クラス名')[インデックス番号]
