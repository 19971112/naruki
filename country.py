import sys

f1 = open ("countrypart.txt","r")
f2 = open ("abbreviation.txt","r").read()

# 空の辞書の作成
dic = {}

# 読み込んだリストのファイルを一行づづ辞書に登録
line = f1.readline()
while line:
    key = line[:line.find(",")]
    value = line[line.find(","):].lstrip(",").strip("\n")
    dic[key] = value
    line = f1.readline()
f1.close()

#　ファイルの読み込み
for k, v in dic.items():
    mystr = f2.replace(k, v)

print(mystr)
