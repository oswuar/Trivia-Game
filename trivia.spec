# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Trivia.py'],
    pathex=[],
    binaries=[],
    datas=[('bienvenida.png', '.'), ('explosion.wav', '.'), ('fondo1.png', '.'), ('fondo2.png', '.'), ('fondo3.png', '.'), ('fondo4.png', '.'), ('fondo5.png', '.'), ('fondo6.png', '.'), ('fondo7.png', '.'), ('fondo8.png', '.'), ('fondo9.png', '.'), ('fondo10.png', '.'), ('fondo11.png', '.'), ('final.png', '.'), ('frog.png', '.'), ('fuego.wav', '.'), ('martillo.wav', '.'), ('morde.png', '.'), ('music.mp3', '.'), ('pike.png', '.')],
    hiddenimports=[],
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
    a.binaries,
    a.datas,
    [],
    name='Trivia',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icono.ico'],
)
