# -*- mode: python -*-

block_cipher = None


a = Analysis(['hangman_beta.py'],
<<<<<<< HEAD
             pathex=['/home/roland/Python/software-testing-project'],
=======
             pathex=['C:\\Users\\dirk_\\OneDrive\\Bureaublad\\CPS\\SWT\\software-testing-project'],
>>>>>>> 59809ceeea62e0cb40c147debbc65967879fd58c
             binaries=[],
             datas=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='hangman_beta',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
