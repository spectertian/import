from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = collect_all('paddleocr')
hiddenimports.extend(['tools', 'paddle', 'paddle.fluid.core'])