import fitz
from PIL import Image
import cv2
import numpy as np
from paddleocr import PPStructure, PaddleOCR, save_structure_res


def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return thresh


# 优化 PPStructure 初始化
table_engine = PPStructure(
    table_model_dir='ppstructure/inference/en_ppstructure_mobile_v2_SLANet',
    table_char_dict_path='ppocr/utils/dict/table_structure_dict_ch.txt',
    layout_model_dir='ppstructure/inference/picodet_lcnet_x1_0_fgd_layout_infer',
    show_log=True,
    image_orientation=True,
    lang='en',
    layout=True,
    table=True,
    ocr=True,
    recovery=True,
    use_angle_cls=True,
    table_max_len=488,
    table_algorithm='TableMaster',
    table_only=True,
    cell_box=True,
    ocr_order_method='tb-lrt',
    det_limit_side_len=736,
    det_limit_type='min',
    det_db_thresh=0.3,
    det_db_box_thresh=0.5,
    rec_model_dir='ppocr/inference/en_PP-OCRv3_rec_infer',
    rec_char_dict_path='ppocr/utils/en_dict.txt',
    rec_image_shape='3,48,320',
    rec_batch_num=6,
    use_gpu=False
)

ocr = PaddleOCR(use_angle_cls=True, lang="en", use_gpu=False)

pdf_document = fitz.open("./doc/20240820200038923.pdf")
page = pdf_document[0]

pix = page.get_pixmap(matrix=fitz.Matrix(3, 2))  # 增加到原来的3倍DPI
img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
img_np = np.array(img)

processed_img = preprocess_image(img_np)

temp_image_path = "temp_image.png"
cv2.imwrite(temp_image_path, processed_img)

result = table_engine(temp_image_path)
print(result)

if not any(block['type'] == 'table' for block in result):
    print("PPStructure未检测到表格，尝试使用PaddleOCR...")
    ocr_result = ocr.ocr(temp_image_path, cls=True)
    for idx, line in enumerate(ocr_result):
        print(f"行 {idx + 1}:")
        for word_info in line:
            print(word_info[1][0])
else:
    print("检测到表格:")
    for block in result:
        if block['type'] == 'table':
            table_data = block['res']
            for row in table_data:
                print(row)
            print("\n")

    # 保存结构化结果
    save_structure_res(result, 'output', temp_image_path)

    # 可视化结果
    from paddleocr import draw_structure_result
    from PIL import Image

    image = cv2.imread(temp_image_path)
    im_show = draw_structure_result(image, result)
    im_show = Image.fromarray(im_show)
    im_show.save('result.jpg')

import os

os.remove(temp_image_path)

pdf_document.close()