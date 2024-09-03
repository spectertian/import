import sys

import fitz  # PyMuPDF
import io
from PIL import Image
from paddleocr import PPStructure, draw_structure_result, save_structure_res
import numpy as np
import cv2


# 初始化PPStructure模型
# table_engine = PPStructure(show_log=True)
table_engine = PPStructure(table_max_len=488,
                           table_model_dir='ppstructure/inference/en_ppstructure_mobile_v2_SLANet',
                           show_log=True)

# 打开PDF文件
pdf_document = fitz.open("./doc/20240820200038923.pdf")

# 获取第一页
page = pdf_document[0]

# 将页面渲染为图像
# pix = page.get_pixmap()
pix = page.get_pixmap(matrix=fitz.Matrix(3, 4))  # 增加到原来的2倍DPI


# 将图像转换为PIL Image对象
image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

# 保存为临时图像文件
temp_image_path = "temp_image.png"
image.save(temp_image_path)

# 使用PPStructure进行表格识别
result = table_engine(temp_image_path)



import pandas as pd

def result_to_df(result):
    data = []
    for item in result:
        if item['type'] == 'table':
            print(item['res']['html'])
            for row in item['res']['html']:
                data.append(row)
    return pd.DataFrame(data)

df = result_to_df(result)
print(df)



sys.exit(1)
# 保存识别结果
save_structure_res(result, 'result', temp_image_path)

# 指定字体文件路径
font_path = "./doc_2/fonts/simfang.ttf"  # 替换为你的字体文件路径

# 绘制识别结果
im_show = draw_structure_result(image, result, font_path=font_path)
# 将NumPy数组转换为PIL Image对象
im_show_pil = Image.fromarray(np.uint8(im_show))
# im_show.save('result.jpg')
cv2.imwrite('result.jpg', cv2.cvtColor(im_show, cv2.COLOR_RGB2BGR))


# 打印识别结果
# for line in result:
#     print(line)

# 清理临时文件
# import os
# os.remove(temp_image_path)

# 关闭PDF文档
pdf_document.close()