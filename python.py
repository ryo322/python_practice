s1 = input("aの値を入力してください＞")
s2 = input("bの値を入力してください＞")

print("s1 + s2 =", (s1 + s2))

a = int(s1)
b = int(s2)

print("a=", a, ",b =", b)
print("a + b =", (a + b))
print("a - b =", (a - b))
print("a * b =", (a * b))
print("a ** b =", (a ** b))
print("a / b =", (a / b))
print("a // b =", (a // b))
print("a % b =", (a % b))

print("a >= 0 :", (a >= 0))
print("(a >= 0) and (b >= 0) :", (a >= 0) and (b >= 0))


#**は累乗で*は掛け算なので注意が必要
#//は整数で計算を切り上げる。/は小数点まで計算

#論理演算子
#and 論理積
#not 否定
#or  論理和

#input(文字列)：文字列を表示して入力された文字列を受け取る関数