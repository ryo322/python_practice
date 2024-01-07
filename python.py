import time
import random

colors = ["黄色", "黄緑", "緑", "水色", "青", "紫", "赤"]

print("あなたの運勢は")
for i in range(3):
    print("　　.")
    time.sleep(1) #処理に１秒かける

fn1 = random.random()
if fn1 >= 0.7:
    print("大吉")
elif fn1 >= 0.4:
    print("中吉")
elif fn1 >= 0.1:
    print("小吉")
else :
    print("凶")

fn2 = random.randint(0, 6)
print("ラッキーカラーは", colors[fn2])

print("fn1:", fn1)
print("fn2:", fn2)

#ライブラリ：よく使う処理を利用しやすくまとめたもの
#モジュール：プログラムの部品（＝ファイル）
#パッケージ：モジュールの集まり

#手順
#①インストール：pip install ライブラリ名
#②プログラムでインポートして読み込む：import モジュール名(as 別名),import パッケージ名.•••.モジュール名
#③ライブラリの機能を呼び出す：モジュール名.変数名、モジュール名.関数名(引数,・・・)