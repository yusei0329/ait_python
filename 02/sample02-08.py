import json
json_open = open('./02/lecture02_json.json', 'r')
j = json.load(json_open)

print(j)
# {'ID': 'k19999', '名前': '愛知太郎', '成績': {'国語': 45, '数学': 90}}
print(type(j))
# <class 'dict'>