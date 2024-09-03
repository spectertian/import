from paddleocr import PPStructure, draw_structure_result, save_structure_res

# 初始化PPStructure模型
table_engine = PPStructure(show_log=True)

# 指定图片路径
img_path = 'path/to/your/image.jpg'

# 使用PPStructure进行表格识别
result = table_engine(img_path)

# 保存识别结果
save_structure_res(result, 'output', img_path)

# 绘制识别结果
from PIL import Image
import cv2
import numpy as np

img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
im_show = draw_structure_result(img, result)
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')

# 打印识别结果
for line in result:
    print(line)