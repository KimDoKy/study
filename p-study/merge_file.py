BUFSIZE = 256*1024
merge_filename = 'merge-python-3.7.3.pkg'
filelist = ['python-3.7.3.pkg_' + str(x) for x in range(9)]

with open(merge_filename, 'wb') as f:
    for filename in filelist:
        print(f'[{filename}] 합치는중..')
        with open(filename, 'rb') as h:
            buf = h.read(BUFSIZE)
            while buf:
                f.write(buf)
                buf = h.read(BUFSIZE)

print('complate')
