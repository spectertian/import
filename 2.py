import threading
from paddleocr import PaddleOCR

import time

def ocr_process(image_path, results, index):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch", det_model_dir='./ch_PP-OCRv4_det_infer')
    result = ocr.ocr(image_path, cls=True)
    results[index] = result

image_paths = ['./pic/1.jpg', './pic/2.jpg', './pic/3.png', './pic/4.png','./pic/5.jpg','./pic/6.jpg','./pic/7.png','./pic/8.png','./pic/9.jpg','./pic/10.png']
threads = []
results = [None] * len(image_paths)

start_time = time.time()

for i, path in enumerate(image_paths):
    thread = threading.Thread(target=ocr_process, args=(path, results, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

for result in results:
    print(result)