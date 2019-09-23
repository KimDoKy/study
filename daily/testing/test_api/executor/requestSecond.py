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
        complate_count = []
        try:
# for i in range(13):
            for i in range(2):
                temp_str = choices(self.string, k=28)
                temp_str2 = ''
                data = {'data':temp_str2.join(temp_str)}
                req = self.session.post(
                        self.url,
                        headers=headers,
                        data=data,
                        timeout=5)
                if req.status_code == 200:
                    complate_count.append(req.status_code)
        except:
            print('err')
            pass
        finally:
            count = len(complate_count)
            print('complate count: ', len(complate_count))
            return count

    def taskDone(self, fn):
        return fn

    def run(self, future, send_end):
        print(a)
        with ThreadPoolExecutor(max_workers=20) as executors:
            results = []
            for i in range(2):
# for i in range(21):
                results.append(executors.submit(self.request_post()))
            total = 0
            for result in results:
                print('result: ', result.result())
#        total += self.taskDone(result)
        send_end.send(total)


if __name__ == '__main__':
    main()
    print(complate_count)
