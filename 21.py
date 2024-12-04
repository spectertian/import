import pytesseract
from PIL import Image
import pandas as pd
import re
import cv2
import numpy as np

def preprocess_image(image_path):
    # 读取图像
    img = cv2.imread(image_path)

    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 应用自适应阈值
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # 降噪
    denoised = cv2.fastNlMeansDenoising(thresh, None, 10, 7, 21)

    return denoised

# 使用预处理后的图像
preprocessed_image = preprocess_image('doc/1.png')

custom_config = r'--oem 3 --psm 6'
preprocessed_image = Image.open('doc/1.png')

text = pytesseract.image_to_string(preprocessed_image, config=custom_config)
# text = pytesseract.image_to_string(preprocessed_image)
# 设置tesseract执行文件的路径（如果需要）
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 读取图像
# image = Image.open('doc/1.png')
#
# # 执行OCR
# text = pytesseract.image_to_string(image)
print(text)

# 将文本分割成行
lines = text.split('\n')

# 创建一个列表来存储数据
data = []

# 正则表达式模式
pattern = r'^(.+?),\s*(.+?)\s+(\w+)\s+(\d{2}:\d{2})\s+(\d{2}:\d{2})\s+(\d{2}:\d{2})\s+(\d{2}:\d{2})'

# 处理每一行
for line in lines:
    match = re.match(pattern, line)
    if match:
        last_name, first_name, position, start_time, end_time, other_time1, other_time2 = match.groups()
        data.append({
            'Last Name': last_name,
            'First Name': first_name,
            'Position': position,
            'Start Time': start_time,
            'End Time': end_time,
            'Other Time 1': other_time1,
            'Other Time 2': other_time2
        })

# 创建DataFrame
df = pd.DataFrame(data)

# 显示结果
print(df)

# 保存到CSV文件
df.to_csv('employee_time_data.csv', index=False)