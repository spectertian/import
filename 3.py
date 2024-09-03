import os
import sys
import fitz  # PyMuPDF
from PIL import Image

import cv2
from paddleocr import PPStructure, draw_structure_result, save_structure_res

table_engine = PPStructure(show_log=True)

# 打开PDF文件
pdf_document = fitz.open("./doc/20240820200038923.pdf")

# 获取第一页
page = pdf_document[0]

# 将页面渲染为图像
pix = page.get_pixmap()

# 将图像转换为PIL Image对象
image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

# 保存为临时图像文件
temp_image_path = "temp_image.png"
image.save(temp_image_path)

# 使用PPStructure进行表格识别
result = table_engine(temp_image_path)

font_path = './doc_2/fonts/simfang.ttf'  # PaddleOCR下提供字体包

# 保存识别结果
save_structure_res(result, 'result', temp_image_path)

# 绘制识别结果
im_show = draw_structure_result(image, result, font_path=font_path)
im_show.save('result.jpg')

# 绘制识别结果
im_show = draw_structure_result(image, result)
im_show.save('result.jpg')

# 打印识别结果
for line in result:
    print(line)

# 清理临时文件
import os

os.remove(temp_image_path)

# 关闭PDF文档
pdf_document.close()
sys.exit(1)

save_folder = './output/table'
img_path = './doc/20240820200038923.pdf'
img = cv2.imread(img_path)
result = table_engine(img)
save_structure_res(result, save_folder, os.path.basename(img_path).split('.')[0])

for line in result:
    line.pop('img')
    print(line)

from PIL import Image

font_path = './doc_2/fonts/simfang.ttf'  # PaddleOCR下提供字体包
image = Image.open(img_path).convert('RGB')
im_show = draw_structure_result(image, result, font_path=font_path)
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')
