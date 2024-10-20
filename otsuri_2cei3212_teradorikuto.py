# -*- coding: utf-8 -*-
"""otsuri_2CEI3212_TeradoRikuto.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IQcej1fSzP4o8uZI2kZjfZUJcIPbidKQ
"""

# 変数
global n
global m
x = 0
y = 0
y500 = 0
y100 = 0
y50 = 0
y10 = 0
otsuri = 0

# 関数
def fusoku():
  global n
  global m

  print('\n投入金額が不足しています。')
  m = int(input('追加する金額を整数で入力してください。1円、５円は使用できません。\n'))

  n += m
  print(f'現在投入されている金額 {n:.0f}円')

def calc():
  global n

  n -= x
  y500,y = n // 500, n % 500
  y100,y = y // 100, y % 100
  y50,y = y // 50, y % 50
  y10,y = y // 10, y % 10

  otsuri = (y500*500 + y100*100 + y50*50 + y10*10)

  print(f'\nおつりは500円玉 {y500:.0f}枚、100円玉 {y100:.0f}枚、50円玉 {y50:.0f}枚、10円玉 {y10:.0f}枚、\n計 {otsuri:.0f} 円です')


# 処理
n = int(input('投入する金額を整数で入力してください。1円、５円は使用できません。\n'))
x = int(input('商品の金額を整数で入力してください。１の位は０にしてください。\n'))

while n < x:
  fusoku()

  if m < x:
    fusoku()
  else:
    break

if n >= x:
  calc()