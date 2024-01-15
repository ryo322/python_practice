dictionary = {
    'A' : '田中',
    'B' : '佐藤',
    'C' : '男性',
    'D' : '東京',
    'E' : '海外旅行',
}

print(dictionary)

dictionary.pop('A') #要素の削除は.pop(削除する項目)
print(dictionary)

dictionary.clear() #.clear()はすべての要素を削除
print(dictionary)
