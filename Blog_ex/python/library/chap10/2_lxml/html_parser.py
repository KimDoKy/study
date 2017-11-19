from lxml import html
import urllib.request

url = 'https://docs.python.org/3.4/library/index.html'
tree = html.parse(urllib.request.urlopen(url)).getroot()
div_toctree = tree.find('.//div[@class="toctree-wrapper compound"]/')

print(html.tostring(div_toctree, pretty_print=True, encoding='unicode'))
