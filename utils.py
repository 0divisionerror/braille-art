from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_str2image(fontname, fontsize, text):
    '''
    文字から画像を作り出す

    Args:
        fontname: 使うフォントのpath
        fontsize: フォントの大きさ
        text    : 文字
    Return:
        なし
    '''
    font = ImageFont.truetype(fontname, fontsize)

    tmp = Image.new('RGB', (1, 1), (255, 255, 255))
    tmp_d = ImageDraw.Draw(tmp)
    textsize = tmp_d.textsize(text, font)

    img = Image.new('RGB', textsize, (255, 255, 255))
    draw = ImageDraw.Draw(img)
    font_color="black"
    draw.text((0,0), text, fill=font_color, font=font)
    img.save("./imgs/image.png")


def num2braille(n):
    '''
    indexから対応する点字を返す関数

    Args:
        n: fragmentの合計値
    Return:
        点字
    '''

    flg = 0
    flg += (n & 0b00001000) << 3
    flg += (n & 0b01110000) >> 1
    flg += (n & 0b10000111)

    return chr(flg + 0x2800)



def preprocess(path, col, rev):
    '''
    画像の読み込み，リサイズ，データ化をする

    Args:
        path: 画像のパス
        col : Widthのサイズ
        rev : 白黒の反転するかしないか(True = する)
    Return:
        img : 画像の行列
    '''
    # 画像の読み込み
    img = Image.open(path)
    img = img.convert('L')

    # 画像サイズを4の倍数にしておくための計算
    width = col * 4
    height = int(width * (img.height / img.width))
    height -= height % 4

    # 画像のリサイズ
    img = img.resize((width, height))
    # 画像のデータ化
    if rev:
        img = thresh_otsu(np.matrix(img), min_value=1, max_value=0)
    else:
        img = thresh_otsu(np.matrix(img))

    return img



def thresh_otsu(g, min_value=0, max_value=1):
    '''
    大津の二値化

    明と暗を２つのクラスに分けて，いい感じのところを見つけるアルゴリズム

    Args:
        g: グレースケールの画像の行列
    Return:
        g: 二値化された画像の行列

    
    参考：
    https://algorithm.joho.info/programming/python/opencv-otsu-thresholding-py/
    '''

    # ヒストグラムの作成
    hist = [np.sum(g == i) for i in range(256)]
    
    s_max = (0, -10)


    for th in range(256):

        # クラス1とクラス2の画素数を計算
        n1 = sum(hist[:th])
        n2 = sum(hist[th:])

        # クラス1とクラス2の画素値の平均を計算
        mu1 = 0 if n1 == 0 else sum([i * hist[i] for i in range(0,th)]) / n1
        mu2 = 0 if n2 == 0 else sum([i * hist[i] for i in range(th, 256)]) / n2
        
        # クラス間分散の分子を計算
        s = n1 * n2 * (mu1 - mu2) ** 2

        # クラス間分散の分子が最大の時，クラス間分散の分子と閾値を記録
        if s > s_max[1]:
            s_max = (th, s)
    
    # クラス間分散が最大の時の閾値を取得
    t = s_max[0]

    #算出した閾値で二値化処理
    g[g < t] = min_value
    g[g >= t] = max_value

    return g
