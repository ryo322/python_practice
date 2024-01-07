def usage():
    print("英語と数学の平均点を計算")
    print("0~100の数値を入力してください")

def display(e, m):
    print("英語は", e, "点")
    print("数学は", m, "点")

def get_avg(e, m):
    a = (e + m) / 2
    return a

usage()

eng = int(input("英語の点数を入力　ー＞"))
math = int(input("数学の点数を入力　ー＞"))

display(eng, math)

avg = get_avg(eng, math)
print("平均は", avg, "点")

#組み込み関数：提供されている関数
#ユーザー定義関数：自分で作る関数

#関数の作り方
#def　関数名　（引数, ・・・）
#引数：呼び出し元から受け取る値
#戻り値：関数の処理の後に呼び出し（もとに返す値はreturn文で指定、指定しない場合はNoneが返る）