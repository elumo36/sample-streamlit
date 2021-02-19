# ２行目のは、ヘッドレスモードにするためのオプションの操作のため
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
#import pandas as pd


# クロムの立ち上げ
browser = webdriver.Chrome()

# Webアクセスする！
URL = "https://scraping-for-beginner.herokuapp.com/login_page"
browser.get(URL)

# 情報の取得して、とあるページのログインをする
elem_user_id = browser.find_element_by_id('username')
elem_user_id.send_keys('imanishi')
password = browser.find_element_by_id('password')
password.send_keys('kohei')
btn = browser.find_element_by_id('login-btn')
btn.click()

# ログインされる、その後値を取得してくる
elem_name = browser.find_element_by_id('name')
# .textで値を取得できる。
name = elem_name.text

# 取得した後、形を整えてあげるといい。
# name.replace("\n",",")

# タグで取得してみる、繰り返し文のときには便利になる,
# ただし、find_elementではダメ、１つしか、取得しない。
#elem_th = browser.find_element_by_tag_name('th')
# .find_elements_by_tag_nameを使う！
elems_th = browser.find_elements_by_tag_name("th")
# リストの形で全て取得出来るので、
#   elems_th[0].text というように出来る。
keys = []
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)


elems_td = browser.find_elements_by_tag_name("td")
# リストの形で全て取得出来るので、
#   elems_th[0].text というように出来る。
values = []
for elem_td in elems_td:
    value = elem_td.text
    values.append(value)

# CSVファイルに出力
#df = pd.DataFrame()
#df['項目'] = keys
#df['値'] = values
# df.to_csv('sample.csv',index=False)

# ヘッドレスモード（CUIのみの処理で完結させる、画面には表示されない）裏で実行中
#options1 = Options()
# options1.add_argument('--headless')
#browser = webdriver.Chrome(options=options1)
#URL = "https://scraping-for-beginner.herokuapp.com/login_page"
# browser.get(URL)
# browser.quit()

# ログインしたあと、自動で摘出する。
