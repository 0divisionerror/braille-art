import sys, os
import argparse
import numpy as np

from utils import create_str2image, preprocess, num2braille

# 使うフォント
FONT_PATH = "./fonts/ipag.ttf"


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="./imgs/sample.png", type=str)
    parser.add_argument("--col", default=32, type=int)
    parser.add_argument("--rev", action="store_true")
    args = parser.parse_args()


    # 画像があるなら画像で生成，無ければ文字から画像をつくる
    if not os.path.isfile(args.input):
        path = create_str2image(FONT_PATH, 32, args.input)
        img = preprocess(path, args.col, args.rev)
    else:
        img = preprocess(args.input, args.col, args.rev)


    braille_list = []
    for i in range(int(np.shape(img)[0]/4)):
        for j in range(int(np.shape(img)[1]/2)):
            
            row = i * 4
            col = j * 2
            # 点字1つ分を取り出す
            fragment = img[row:row+4, col:col+2]
            
            # バイナリから合計値を出して最適な点字を算出する
            b = 0
            for r in range(np.shape(fragment)[0]):
                for c in range(np.shape(fragment)[1]):
                    b += (fragment[r, c]) << r + c * 4

            braille_list.append(num2braille(b))

        braille_list.append('\n')

    # 書き出す
    for i in braille_list:
        sys.stdout.write(i)