# import
# pip install  PySide6
# pip install  paddleocr  paddlepaddle
# pip install Pillow
# pip install opencv-python
# pip install PyMuPDF
# pip install shapely
# pip install openpyxl
# pip install pandas
# pip install PyMuPDF opencv-python Pillow paddleocr paddlepaddle shapely openpyxl
# pip install cython

# pip install pyinstaller
# python setup.py build_ext --inplace
# --additional-hooks-dir hook-paddleocr.py
# pyinstaller 122.spec


```
pyinstaller --name=MyApp --onefile --windowed --additional-hooks-dir=./hooks --hidden-import  --add-binary "C:\Windows\System32\msvcp140.dll;." --add-binary "C:\Windows\System32\vcruntime140.dll;." paddleocr 700.py

```