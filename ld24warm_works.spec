# -*- mode: python -*-
a = Analysis(['../ld24warmup/ld24warm.py'],
             pathex=['/Users/fistel/Developer/pyinstaller-2.0'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build/pyi.darwin/ld24warm', 'ld24warm'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas + [('bu-woeful-matrices.it','/Users/fistel/Developer/ld24warmup/bu-woeful-matrices.it','DATA'),
                          ('chicken.png','/Users/fistel/Developer/ld24warmup/chicken.png','DATA'),
                          ('ship.png','/Users/fistel/Developer/ld24warmup/ship.png','DATA'),
                          ('Laser_Squeak.wav','/Users/fistel/Developer/ld24warmup/Laser_Squeak.wav','DATA'),
                          ('Retro_Death.wav','/Users/fistel/Developer/ld24warmup/Retro_Death.wav','DATA')],
               strip=None,
               upx=True,
               name=os.path.join('dist', 'ld24warm'))
