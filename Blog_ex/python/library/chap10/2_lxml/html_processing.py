from lxml import html
import urllib.request

url = 'https://docs.python.org/3.4/library/index.html'
tree = html.parse(urllib.request.urlopen(url)).getroot()
div = tree.find('.//div[@class="toctree-wrapper compound"]/')

for tag in div.xpath('//*[@class]'):
    tag.attrib.pop('class')

absolute_url = html.make_links_absolute(div, base_url="http://docs.python.org/3.4/library/")

print(html.tostring(absolute_url, pretty_print=True, encoding='unicode'))
