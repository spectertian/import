import fitz
from PIL import Image
import cv2
import re
import numpy as np
from paddleocr import PPStructure, PaddleOCR

pattern = r'^[a-zA-Z,\s]+$'


def is_valid(text):
    return bool(re.match(pattern, text))


ss = [
    ' Hereford, Nathaniel Stephen ',
    'FFT2',
    '20:00',
    '22:00',
    '0:00',
    '0:00',
    'Braden, Brandon wefew',
    'FFT2',
    '20:00',
    '22:00',
    '0:00',
    '0:00',
    'Braden, werew Derek',
    'FFT2',
    '20:00',
    '22:00',
    '0:00',
    '0:00',
    '1REMARK',
]
data = {}
# re_data =
data['date'] = ''
data['list'] = []
re_ss = []

i_index = 0
for word_info in ss:
    i_index = i_index + 1

    if word_info == "1REMARK":
        print(re_ss)
        data['list'].append(re_ss)
        re_ss = []
        break
    print(word_info)  # 打印识别的文字

    if i_index == 7:
        data['date'] = word_info
        # continue

    if i_index >= 1:
        if is_valid(word_info.strip()):
            if i_index > 1:
                print("save")
                print(re_ss)
                data['list'].append(re_ss)
                re_ss = []

            re_ss.append(word_info.strip())
        else:
            # print(word_info.strip())
            re_ss.append(word_info.strip())
            print(re_ss)

print(data)
