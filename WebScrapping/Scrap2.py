from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import json

url = 'https://www.dsebd.org/news_archive_7days.php'

uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

#print(str(page_soup.body.div.table))
#print(str(page_soup.findAll('td'))) #{'class': 'class_name'}

trs = page_soup.findAll('tr')
i = 0
News_list = []

while i < len(trs):
    if i>2:
        tds = trs[i].findAll('td')
        Trading_Code = tds[1].text
        i += 1

        tds = trs[i].findAll('td')
        Title = tds[1].text
        i += 1

        tds = trs[i].findAll('td')
        News = tds[1].text
        i += 1

        tds = trs[i].findAll('td')
        Post_Date = tds[1].text
        i += 1

        diccc = {
            'Trading_Code': Trading_Code,
            'Title': Title,
            'News': News,
            'Post_Date': Post_Date
        }

        News_list.append(diccc)
    i=i+1


#print(News_list[1])
json_array = json.dumps(News_list)
print(json_array)
