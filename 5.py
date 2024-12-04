import fitz
from PIL import Image
import cv2
import numpy as np
from paddleocr import PPStructure, PaddleOCR

def preprocess_image(image):
    # 转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 二值化
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return thresh

# 初始化PPStructure和PaddleOCR模型
table_engine = PPStructure(show_log=True)
ocr = PaddleOCR(use_angle_cls=True, lang="en", use_gpu=False)

# 打开PDF文件
pdf_document = fitz.open("./doc/20240820200038923.pdf")

# 获取第一页
page = pdf_document[0]

# 将页面渲染为图像
pix = page.get_pixmap(matrix=fitz.Matrix(4, 3))  # 增加到原来的2倍DPI
img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
img_np = np.array(img)

# 预处理图像
processed_img = preprocess_image(img_np)

# 保存为临时图像文件
temp_image_path = "temp_image.png"
cv2.imwrite(temp_image_path, processed_img)

# 使用PPStructure进行表格识别
result = table_engine(temp_image_path)

# 如果没有识别出表格，尝试使用PaddleOCR
if not any(block['type'] == 'table' for block in result):
    print("PPStructure未检测到表格，尝试使用PaddleOCR...")
    ocr_result = ocr.ocr(temp_image_path, cls=True)
    for idx, line in enumerate(ocr_result):
        print(f"行 {idx+1}:")
        print(line)
        for word_info in line:
            print(word_info[1][0])  # 打印识别的文字
else:
    # 输出表格数据
    for block in result:
        if block['type'] == 'table':
            print("检测到表格:")
            table_data = block['res']
            for row in table_data:
                print(row)
            print("\n")

# 清理临时文件
import os
os.remove(temp_image_path)

# 关闭PDF文档
pdf_document.close()