dictionary = {
    'A' : '田中',
    'B' : '佐藤',
    'C' : '男性',
    'D' : '東京',
    'E' : '海外旅行',
}

print(dictionary)

print(dictionary.keys())

print(dictionary.values())

print('男性' in dictionary.values())

for key, value in dictionary.items():
    print(f'キーは{key}, バリューは{value}')
