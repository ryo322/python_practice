price_str = input("税抜き金額を入力してください")
rate = 0.10
price = int(price_str)

if price >= 5000:
    discount = 500
elif price >= 3000:
    discount = 300
else:
    discount = 0

amount = int((price - discount) * (1 + rate))

print("値引金額：", discount, "円")
print("税込金額：", amount, "円")