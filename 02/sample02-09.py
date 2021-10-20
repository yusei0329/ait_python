import json

h = dict([(0,'国語'),(1, '数学'),(2, '理科'),(3, '社会'),(4, '英語')])
print(json.dumps(h, ensure_ascii=False)) # `ensure_ascii=False`を付けないとユニコードが表示される
# {"0": "国語", "1": "数学", "2": "理科", "3": "社会", "4": "英語"}
# {"0": "\u56fd\u8a9e", "1": "\u6570\u5b66", "2": "\u7406\u79d1", "3": "\u793e\u4f1a", "4": "\u82f1\u8a9e"}

with(open('./02/class_names.json','w')) as f:
    json.dump(h, f, indent=4, ensure_ascii=False) # or f.write(json.dumps(h, ensure_ascii=False))