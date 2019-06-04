from zipfile import *
import os

def compressDir(zipname, folder):
    print(f'compress [{folder}] -> [{zipname}]...')
    with ZipFile(zipname, 'w') as ziph:
        for dirname, subdirs, files in os.walk(folder):
            for file in files:
                ziph.write(os.path.join(dirname, file))

folder = 'temp_dir'
zipname = folder + '.zip'
compressDir(zipname, folder)

# os.walk('dirname') : dirname 아래의 디렉터리와 파일들을 탐
