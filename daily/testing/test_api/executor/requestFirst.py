import requests
from random import choices
import string
import time
from concurrent.futures import ThreadPoolExecutor

class RequestPost:

    def __init__(self, url):
        self.url = url
        self.string = string.ascii_letters
        self.session = requests.Session()

    def request_post(self):
        headers = {'Content-Type':'application/json; charset=utf-8'}
        for i in range(167):
            temp_str = choices(self.string, k=28)
            temp_str2 = ''
            data = {'data':temp_str2.join(temp_str)}
            req = self.session.post(self.url, headers=headers, data=data)

    def run(self):
        with ThreadPoolExecutor(max_workers=20) as executors:
            p1=executors.submit(self.request_post())
            p2=executors.submit(self.request_post())
            p3=executors.submit(self.request_post())
            p4=executors.submit(self.request_post())
            p5=executors.submit(self.request_post())
            p6=executors.submit(self.request_post())
            p7=executors.submit(self.request_post())
            p8=executors.submit(self.request_post())
            p9=executors.submit(self.request_post())
            p10=executors.submit(self.request_post())
            p11=executors.submit(self.request_post())
            p12=executors.submit(self.request_post())
            p13=executors.submit(self.request_post())
            p14=executors.submit(self.request_post())
            p15=executors.submit(self.request_post())
            p16=executors.submit(self.request_post())
            p17=executors.submit(self.request_post())
            p18=executors.submit(self.request_post())
            p19=executors.submit(self.request_post())
            p20=executors.submit(self.request_post())

if __name__ == '__main__':
    main()
