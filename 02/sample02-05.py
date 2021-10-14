# 文字列をstr1に代入
str1 = '私は学籍番号k19999の愛知で、豊田市八草町在住です。'

# 部分文字列を取り出す．
print(f'str1のindex 6から12を取り出すと"{str1[6:12]}"です．')
# str1のindex 6から12を取り出すと"k19999"です．

# ヒアドキュメント(バックスラッシュ\が入ると改行とみなされない)
str2 =f"""\
これから自己紹介をします。
{str1}\
"""
print(str2)

# 改行文字を探して分割
for line in str2.split("\n"):
    print(line)

# 改行文字を探して分割２
[print(line) for line in str2.split("\n")]

# 1行ずつ文字数を数える
[len(line) for line in str2.split("\n")]

# 1行ずつ指定した文字列が含まれているかを判定する
[line.find("。") for line in str2.split("\n")]
# [12, 27] 含まれている場合，先頭からのindexが返される（参考：index, rfind, rindex）
[line.find("学籍番号") for line in str2.split("\n")]
# [-1, 2] 含まれていない場合は-1が返される
[line.find("自己紹介") for line in str2.split("\n")]
# [4, -1] 含まれていない場合は-1が返される

# str1から学籍番号とそのindexを正規表現で探し表示する
import re
matchObj = re.search(r'[kx][\d]{5}', str1)
if matchObj:
    print(matchObj.group())
    print(matchObj.span())
# k19999
# (6, 12)

# str1から学籍番号の部分文字列を取り出す
matchObj = re.search(r'[kx][\d]{5}', str1)
id = '' # 文字列として初期化
if matchObj:
    id = str1[matchObj.span()[0]:matchObj.span()[1]]


print(id)
# 学籍番号が含まれていれば'k19999'のように学籍番号を，含まれていなければ空文字''を出力