import requests
from bs4 import BeautifulSoup


def getLinksYoutube(search_text):
    page = 1
    max_page =2

    url = "https://m.youtube.com/results?search_query="+str(search_text)

    source_code = requests.get(url)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text, features="html.parser")
    #print(plain_text)
    i = 0
    for link in soup.findAll('a',{'class': 'yt-uix-sessionlink'}): #,{'id': 'yt-uix-sessionlink'}
        href = link.get('href')
        if(href[0:6] == '/watch'):
            print(href)
            i+=1

    print(i)


getLinksYoutube('nahid');