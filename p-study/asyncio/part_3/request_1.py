import requests
import time
from bs4 import BeautifulSoup as bs

def get_text_from_url(url):
    print(f'Send request to ...{url}')
    res = requests.get(url, headers={'user-agent':'Mozilla/5.0'})
    print(f'Get response from ...{url}')
    text = bs(res.text, 'html.parser').text
    return text

if __name__ == '__main__':
    start = time.time()

    base_url = 'https://www.macmillandictionary.com/us/dictionary/american/{keyword}'
    keywords = ['hi', 'apple', 'call', 'feel', 'hello', 'bye', 'like', 'love']
    urls = [base_url.format(keyword=keyword) for keyword in keywords]
    for url in urls:
        text = get_text_from_url(url)
        print(text[:100].strip())
    end = time.time()
    print(f'time taken: {end-start}')
