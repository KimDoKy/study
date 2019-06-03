from zipfile import *

def compressZip(zipname, filename):
    print(f'compress [{filename}] -> [{zipname}] ...')
    with ZipFile(zipname, 'w') as ziph:
        ziph.write(filename)

    print('complate')

filename = 'python-3.7.3.pkg'
zipname = filename + '.zip'
compressZip(zipname, filename)

# ZIP 파일을 사용하려면 ZipFile 객체를 쓰기모드로 생성해야함
