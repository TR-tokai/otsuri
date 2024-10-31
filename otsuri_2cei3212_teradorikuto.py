# 硬貨投入、商品金額設定
def buy(n, m, checkOneFiveYen):
    n = int(input('投入する金額を整数で入力してください。\n'))
    x = int(input('商品の金額を整数で入力してください。１の位は０にしてください。\n'))
    eX = x % 10
    x -= eX

    print(f'投入金額 {n:.0f}円 商品金額 {x:.0f}円')
    if not n % 10 == 0:
        n = error(n, m, checkOneFiveYen)
    else:
        pass

    return n, x

# １円、５円投入エラー
def error(n, m, checkOneFiveYen):
    if n % 10 in checkOneFiveYen or m % 10 in checkOneFiveYen:
        e = n % 10
        n -= e

        print('\n１円玉と５円玉は使えません。返却します。')
        print(f'返却された金額 {e:.0f}円')
        print(f'現在投入されている金額 {n:.0f}円')

        return n

# 投入金額不足
def notEnough(n, checkOneFiveYen):
    print('\n投入金額が不足しています。')
    m = int(input('追加する金額を整数で入力してください。\n'))

    if m % 10 in checkOneFiveYen:
        error(n, m, checkOneFiveYen)
    else:
        n += m
        print(f'現在投入されている金額 {n:.0f}円')

    return n, m

# おつり計算
def calc(n, x, y, y_FiveHundred, y_OneHundred, y_Fifty, y_Ten):
    n -= x
    y_FiveHundred,y = n // 500, n % 500
    y_OneHundred,y = y // 100, y % 100
    y_Fifty,y = y // 50, y % 50
    y_Ten,y = y // 10, y % 10

    otsuri = (y_FiveHundred*500 + y_OneHundred*100 + y_Fifty*50 + y_Ten*10)

    print(f'\nおつりは500円玉 {y_FiveHundred:.0f}枚、100円玉 {y_OneHundred:.0f}枚、50円玉 {y_Fifty:.0f}枚、10円玉 {y_Ten:.0f}枚、\n計 {otsuri:.0f} 円です。')

# メイン処理
def main(n, x, m):
    y = 0
    y_FiveHundred = 0
    y_OneHundred = 0
    y_Fifty = 0
    y_Ten = 0
    checkOneFiveYen = list(range(1, 10))

    n, x  = buy(n, m, checkOneFiveYen)
    #print(n)
    #print(x)

    while n < x:
        n, m = notEnough(n, checkOneFiveYen)
        #print(n)
        if m < x:
            n, m = notEnough(n, checkOneFiveYen)
        else:
            break

    if n >= x:
        calc(n, x, y, y_FiveHundred, y_OneHundred, y_Fifty, y_Ten)


main(n=0, x=0, m=0)
