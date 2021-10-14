#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

# 要素がすべて整数のリスト型のオブジェクトvを受け取り，要素の合計，最大値，最小値をそれぞれ出力する関数を作成せよ．
def lecture01_02(v: list[int, ...]) -> (int, int, int):
  print(f'vの最大値は{np.sum(v)}')
  print(f'vの最大値は{np.max(v)}')
  print(f'vの最小値は{np.min(v)}')
  

# (ヒント：a=[1,5,8,2]などを試しに関数に与えてみて，正しく動作することを確認すること．)
if __name__ == '__main__':
    a=[1,5,8,2]
    lecture01_02(a)