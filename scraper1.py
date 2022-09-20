# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

def get_soup(url:str)->BeautifulSoup:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser") 
    return soup('a')
# Retrieve all of the anchor tags
tags = get_soup(url)

for time in range(count-1):
    tmp_url = tags[pos-1].get('href', None)
    print(tmp_url)
    tags =  get_soup(tmp_url)
print(tags[pos-1].contents[0])