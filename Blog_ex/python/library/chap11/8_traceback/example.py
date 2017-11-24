import traceback

def hoge():
    tuple()[0]

try:
    hoge()
except IndexError:
    print('--- Exception occurred ---')
    traceback.print_exc(limit=None)
