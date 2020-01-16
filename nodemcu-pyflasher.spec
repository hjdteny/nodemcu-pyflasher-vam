# -*- mode: python ; coding: utf-8 -*-
from config import EXENAME, VERSION

block_cipher = None

a = Analysis(['nodemcu-pyflasher.py'],
             pathex=['C:\\Users\\JENT\\dev\\projects\\nodemcu-pyflasher-vam-xp-chinese'],
             binaries=[],
             datas=[("images", "images")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='%s-%s' % (EXENAME, VERSION),
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False, icon='images\\icon-256.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='nodemcu-pyflasher')
