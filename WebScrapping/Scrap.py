from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import json

url = 'https://www.dsebd.org/latest_share_price_all.php'

uClient = uReq(url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, 'html.parser')

#print(str(page_soup.body.div.table))
#print(str(page_soup.findAll('td'))) #{'class': 'class_name'}
share_list = []
items = page_soup.findAll('tr')
k = 0
for i in items:
    if k>0:
        tds = i.findAll('td')
        diccc = {
            '#': tds[0].text,
            'TRADING_CODE': tds[1].text,
            'LTP': tds[2].text,
            'HIGH': tds[3].text,
            'LOW': tds[4].text,
            'CLOSEP': tds[5].text,
            'YCP': tds[6].text,
            'CHANGE': tds[7].text,
            'TRADE': tds[8].text,
            'VALUE': tds[9].text,
            'VOLUME': tds[10].text,

        }
        share_list.append(diccc)
    else:
        k = k+1


print(len(share_list))
json_array = json.dumps(share_list)
print(json_array)