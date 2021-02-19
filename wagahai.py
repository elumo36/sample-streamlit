#pathlibモジュールから、Pathオブジェクトを取り込む
#pathlibモジュールは、ファイルやフォルダを操作するモジュー
from pathlib import Path
#引数が空白なのは、このフォルダを指定するため、パスはなくていいので。

tfile = open("wagahai.html",encoding="utf-8")
text = tfile.read()
tfile.close()

#gyou = text.find("別段激した様子")

#ここで、変換する
text = text.replace("くをそいだような","\n\n\n\n\n\n\n\n")

#書き込みモードで書き込む
wfile = open("wagahai2.html",encoding="utf-8", mode="w")
#書き込む
wfile.write(text)
wfile.close()



