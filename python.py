num = [0, 1, 2, 3]
for i in num:
    print("i =", i)

for j in range(3):
    print("j =", j)

k = 0
while k < 3:
    print("k =", k)
    k = k + 1

sub_name = ["英語", "数学", "国語"]
score = [90, 85, 80]
sum_score = 0

for i in range(3):
    print(sub_name[i], ":", score[i], "点")
    sum_score = sum_score + score[i]

avg = sum_score / 3

print("合計：", sum_score, "点")
print("平均：", avg, "点")

#range(終了値)：０から（終了値−１）までのイテラブルを得る関数
#イテラブル：反復可能な複数のデータに集まり