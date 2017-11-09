import requests
import os
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

# 검색한 웹툰의 ID 값을 구하기
def find_num(main_toon):
    div = main_toon.find('div','list_area daily_all')
    result_title = div.find('a',{'title':search_title})
    start_num = result_title['href'].find('Id=')
    end_num = result_title['href'].find('&we')
    title_id = result_title['href'][start_num+3:end_num]
    return title_id

title_id = find_num(main_toon)

choice_num = input("다운받을 회차를 입력하세요. : ")

title_url = comic_url + title_id + "&no=" + choice_num

# 웹툰 이미지의 주소 및 이미지 파일 추출
toon_bs = bsObj(title_url)
toon_img = toon_bs.find_all('img', {'alt':'comic content'})

dirname = os.path.dirname(os.path.abspath('__file__')) + '/' + search_title

if not os.path.isdir(dirname):
    os.mkdir(search_title)
    os.chdir(search_title)
    os.mkdir(choice_num)
else:
    os.chdir(search_title)
    os.mkdir(choice_num)

path = os.getcwd()
print(path)

for num in range(len(toon_img)):
    img_url = toon_img[num]['src']
    print(img_url)
    file_name = str(num) + '.jpg'
    file_path = path + '/' + choice_num + '/' + file_name
    print(file_path)
    headers = {'Referer':img_url}
    image_file_data = requests.get(img_url, headers=headers).content
    open(file_path, 'wb').write(image_file_data)

