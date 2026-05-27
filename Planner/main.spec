# -*- mode: python ; coding: utf-8 -*-
a = Analysis(['main.py'], pathex=[], binaries=[], datas=[], hiddenimports=[], hookspath=[], runtime_hooks=[], excludes=[], noarchive=False)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, name='app', debug=False, console=False)
