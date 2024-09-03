from paddleocr import PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="ch", det_model_dir='./ch_PP-OCRv4_det_infer')
result = ocr.ocr('./pic/0ce7efcf475fa8cf56360772da2baeb.jpg')
for line in result:
    print(line)
