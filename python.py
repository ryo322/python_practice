msg = ["勉強は", "大変だけど"]
print("msg  ->", msg)

msg.append("前に進もう")
print("append ->", msg)

msg.remove("大変だけど")
print("remove ->", msg)

msg.insert(1,"楽しい")
print("insert ->", msg)

msg.clear()
print("clear ->", msg)

#メソッド：特定の方で使える関数
#append(値)：追加　　例）score.append(85)
#insert(添字、値)：挿入　　例）score.insert(2,90)
#remove(値)：削除　　例）score.remove(75)
#clear()：全削除　　例）score.clear()