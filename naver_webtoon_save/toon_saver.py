from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

comic_url = 'http://comic.naver.com/webtoon/list.nhn?titleId='
url = 'http://comic.naver.com/webtoon/weekdayList.nhn'

html = urlopen(url)

bsObj = BeautifulSoup(html, "html.parser")

title = input("웹툰 제목을 입력하세요. : ")

a = bsObj.find_all('a')

def toon_id(title):
    for toon in a:
        if title in toon:
            href = toon['href']
            start = href.find('Id=')
            return(href[start+3:-12])

title_id = toon_id(title)
toon_url = comic_url + title_id
print(toon_url)


toon_html = urlopen(toon_url)

toon_page = BeautifulSoup(toon_html, 'html.parser')

td = toon_page.find_all('td')

def last_num(td):
    for s in td:
        if 'titleId' in str(s):
            a = s.find('a')['href']
            start = a.find('no=')
            end = a.find('&week')
            num = a[start+3:end]
            print(num)
            return num
            break

toon_id = last_num(td)
detail_url = 'http://comic.naver.com/webtoon/detail.nhn?titleId=%s&no=%s' % (title_id,toon_id)
print(detail_url)

bs_img_html = urlopen(detail_url)
bs_img = BeautifulSoup(bs_img_html, 'html.parser')
content_url = bs_img.find_all('img', {'alt':'comic content'})

img_url = content_url[0]['src']
print(img_url)
headers = {'Referer': img_url}
image_file_data = requests.get(img_url, headers=headers).content
open('test.jpg', 'wb').write(image_file_data)
