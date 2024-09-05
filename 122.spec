# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['700.py'],
    pathex=[],
    binaries=[('msvcp140.dll', 'C:\\Windows\\System32\\msvcp140.dll', 'BINARY'),
        ('vcruntime140.dll', 'C:\\Windows\\System32\\vcruntime140.dll', 'BINARY'),],
    datas=[],
    hiddenimports=['paddle', 'paddle.fluid', 'paddle.fluid.core', 'paddle.fluid.framework'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='your_script',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='anys_pdf',
)
