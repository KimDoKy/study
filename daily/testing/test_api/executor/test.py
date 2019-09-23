print('test')
from requestFirst import *

if __name__ == '__main__':
    a = RequestPost('http://localhost:8000/post/')
    a.run()

