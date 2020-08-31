# 8点点字で絵を描くやつ
8点点字を利用して文字や絵のブライユアート(?)を作ることができます。

## 必要なもの
- numpy
- pillow

### Install
```command
pip install numpy
pip install pillow
```

## 使い方
1. このリポジトリをクローンする。
2. `python main.py`で実行する。

## パラメータ
|引数|説明|属性|
|:--|:--|:--|
|input|画像のパス，もしくは文字|str|
|col|点字の横列の数|int|
|rev|反転するかどうか|-|

### Example
```command
python main.py --input ./imgs/画像
```

```command
python main.py --input ぽんぽこはやおき --col 64 --rev
```

## フォント
IPAゴシック(Ver.003.03)を利用しています。
変更したい場合は，`FONT_PATH`を変更してください。


## 参考にさせて頂いたもの
- [月で絵を描きたいだと？それならpythonに任せなさい](https://qiita.com/wataoka/items/261fc12c956a517049d8)
- [Unicodeの点字でお絵かき](https://qiita.com/zakuroishikuro/items/15d1a69178895edf9a21#8%E7%82%B9%E7%82%B9%E5%AD%97)
