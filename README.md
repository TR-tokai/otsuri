# おつり枚数判定システム
## 基本仕様
- プログラミング言語: python
- 開発: Visual Studio Code
## 使用方法
1. 投入する金額を整数で入力（１円玉と５円玉を含む整数にした場合、１円玉と５円玉が返却される）
2. 購入する商品の金額を整数で入力（１円と５円は使えないため１の位は０にする。もし０にしなかった場合、自動的に１の位は切り捨てられる）

3. 投入金額が不足している場合、お金の追加投入が求められるため、追加する金額を整数で入力する（１円玉と５円玉を含む整数にした場合、１円玉と５円玉が返却される）

   使用方法3番は投入金額が不足している限り繰り返され、都度、現在投入されている金額が表示される
4. 投入金額が商品の金額以上になった場合おつりが計算され、500円・100円・50円・10円の枚数と合計が表示される

## バグ
1. 追加金額入力の際、１の位を０以外にすると返却金額が正しく表示されず、投入金額に加算もされない。
2. 追加金額入力の際、１の位を０以外にし、４桁以上にすると強制終了する。
3. ~~投入金額の１の位を０にするとエラーが出る~~　修正済み
