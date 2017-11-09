import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

comic_url = 'http://comic.naver.com/webtoon/detail.nhn?titleId='
url = 'http://comic.naver.com/webtoon/weekday.nhn'

# BS 객체 생성
def bsObj(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    return bsObj

# 웹툰 메인 페이지 BS 객체화
main_toon = bsObj(url)

search_title = str(input("검색할 웹툰은? "))

div = main_toon.find('div','list_area daily_all')
result_title = div.find('a',{'title':search_title})

def find_num(result):
    start_num = result['href'].find('Id=')
    end_num = result['href'].find('&we')
    title_id = result['href'][start_num+3:end_num]
    return title_id

title_id = find_num(result_title)
choice_num = input("다운받을 회차를 입력하세요. : ")
title_url = comic_url + title_id + "&no=" + choice_num
print(title_url)

toon_bs = bsObj(title_url)
toon_img = toon_bs.find_all('img', {'alt':'comic content'})

for num in range(len(toon_img)):
    img_url = toon_img[num]['src']
    print(img_url)
    n = str(img_url[-7:-4]) +  '.jpg'
    print(n)
    headers = {'Referer':img_url}
    image_file_data = requests.get(img_url, headers=headers).content
    open(n,'wb').write(image_file_data)
