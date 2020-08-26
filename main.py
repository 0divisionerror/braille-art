import numpy as np
import sys
from utils import create_str2image, preprocess, num2braille


WIDTH_SIZE = 20
IMAGE_URL = "./imgs/image.png"
REVERSAL = False

if __name__ == "__main__":

    # 文字を利用する場合
    # create_str2image("./fonts/ipag.ttf", 32, "イ")


    img = preprocess(IMAGE_URL, WIDTH_SIZE, REVERSAL)

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