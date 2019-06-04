from urllib.request import urlopen

BUFSIZE = 256*1024

fileurl = "https://www.python.org/ftp/python/3.7.3/python-3.7.3-macosx10.9.pkg"
filename = fileurl.split('/')[-1]

try:
    with urlopen(fileurl) as f:
        with open(filename, 'wb') as h:
            buf = f.read(BUFSIZE)
            while buf:
                h.write(buf)
                buf = f.read(BUFSIZE)
except Exception as e:
    print(e)


# fileurl을 BUFSIZE만큼 읽어 buf로 지정하고 while문 진입
# 로컬 파일인 filename에 buf로 지정된 데이터를 저장하고, fileurl에서 다시 BUFSIZE만큼 읽고 buf로 두는 반복을 buf에 데이터가 담기지 않을때까지 반복
