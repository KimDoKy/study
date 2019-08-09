from selenium import webdriver
import requests
import os

url = str(input('url을 입력하세요. '))
dir_name = str(input('폴더명: '))
driver = webdriver.Chrome('../../driver/chromedriver')

dirname = os.path.dirname(os.path.abspath('__file__')) + '/' + dir_name
if os.path.isdir(dirname):
    os.chdir(dirname)
else:
    os.mkdir(dirname)
    os.chdir(dirname)
path = os.getcwd()
driver.get(url)
img = driver.find_elements_by_tag_name('img')
for i, v in enumerate(img):
    img_src = v.get_attribute('src')
    img_name = str(i) + '.jpg'
    print(img_name)
    file_path = path + '/' + img_name
    headers = {'Referer': img_src}
    img_response = requests.get(img_src, headers=headers)
    if img_response.status_code == 404:
        break
        driver.close()
    img_file_data = img_response.content
    open(file_path, 'wb').write(img_file_data)

driver.close()
