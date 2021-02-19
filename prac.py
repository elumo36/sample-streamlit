from datetime import date, timedelta
start = date(2021,2,11)
for d in range(4):
    cur = start + timedelta(days=d)
    print( cur )



rfile = open("sample.txt",encoding="utf-8")
text = rfile.read()
rfile.close()
text = text.replace("こ","山")
print(text)
#mode="w"で書き込みモードになる。
wfile = open("sample2.txt",encoding="utf-8", mode="w")
#書き込む
wfile.write(text)
wfile.close()

#pathlibモジュールから、Pathオブジェクトを取り込む
#pathlibモジュールは、ファイルやフォルダを操作するモジュー
from pathlib import Path
#引数が空白なのは、このフォルダを指定するため、パスはなくていいので。
path = Path()
#path.glob  pathオブジェクトの中身（ファイル名）を取得
for filepath in path.glob('*.py'):
    print(filepath)



from pathlib import Path
terms = {"e":0, "b":0}
path = Path()
#path.glob  pathオブジェクトの中身（ファイル名）を取得
for filepath in path.glob('*'):
    #ファイルの中身
    rfile = open(filepath,encoding="utf-8")
    text = rfile.read()
    rfile.close()
    for term in terms:
        cnt = text.count(term)
        terms[term] += cnt
print(terms)
