filename = 'python-3.7.3.pkg'
subsize = 1024*1024*3 # 3MB
suffix = 0

with open(filename, 'rb') as f:
    buf = f.read(subsize)
    while buf:
        subfilename = filename + '_' + str(suffix)
        with open(subfilename, 'wb') as h:
            h.write(buf)
            print(f'[{subfilename}%] complate')

        buf = f.read(subsize)
        suffix += 1
