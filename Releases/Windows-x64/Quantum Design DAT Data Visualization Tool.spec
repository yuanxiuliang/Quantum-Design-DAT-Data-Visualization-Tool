# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['..\\..\\Quantum Design DAT Data Visualization Tool.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib.tests', 'pandas.tests', 'numpy.tests', 'unittest', 'pytest', 'scipy', 'sklearn', 'IPython', 'jupyter', 'notebook', 'sphinx', 'setuptools', 'pip', 'wheel', 'distutils', 'pydoc', 'doctest', 'pdb', 'profile', 'pstats', 'cProfile'],
    noarchive=False,
    optimize=2,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [('O', None, 'OPTION'), ('O', None, 'OPTION')],
    name='Quantum Design DAT Data Visualization Tool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
