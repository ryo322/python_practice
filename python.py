import requests
import json

zip = input("郵便番号を入力　ー＞")

url = "https://zipcloud.ibsnet.co.jp/api/search"
param = {"zipcode": zip}

res = requests.get(url, param)

data = json.loads(res.text)
print(data["results"][0]["address1"], ¥ #¥はプログラム内で改行する記述
      data["results"][1]["address2"], ¥
      data["results"][2]["address3"])

#API ＝　プログラムの機能を外部から使う仕組み
#Web上で使えるAPIをWebAPIという