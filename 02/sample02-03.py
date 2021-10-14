import numpy as np

# 定数は大文字アンダースコアで区切るなどルールを決めておくと良い
RANGE_NUM = 10

# サイコロを10回振って出た目をlistに入れる
dice_numbers = [np.random.randint(6) for i in range(RANGE_NUM)]

print(dice_numbers)

# サイコロを10回振って偶数の場合だけ取り出しlistに入れる
dice_numbers_even = [x for x in [np.random.randint(6)+1 for i in range(RANGE_NUM)] if x%2==0]

print(dice_numbers_even)