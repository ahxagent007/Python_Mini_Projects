import requests
from bs4 import BeautifulSoup


def getImageLinks(search_text):

    url = "https://www.google.com/search?tbm=isch&sxsrf=ACYBGNSJVfeRJkMDChH1jKpaEeX1CBRGVw%3A1582046376993&source=hp&biw=1920&bih=937&ei=qBxMXsW8Ooa1rQGUxprwDQ&q="+search_text+"&oq=nature&gs_l=img.3..35i39l2j0l4j0i131j0l3.22144.22755..22771...0.0..0.110.281.2j1......0....1..gws-wiz-img.9uJTZJIujGo&ved=0ahUKEwjFsMSCztvnAhWGWisKHRSjBt4Q4dUDCAY&uact=5"

    source_code = requests.get(url)
    plain_text = source_code.text

    soup1 = BeautifulSoup(plain_text, features="html.parser")
    #print(plain_text)

    for link in soup1.findAll('img', class_='n3VNCb'):  # ,{'id': 'yt-uix-sessionlink'}
        #href = link.get('src')
        print(link.text)
        print(type(link))

    for link in soup1.findAll('a',{'class': 'wXeWr'}): #,{'id': 'yt-uix-sessionlink'}
        href = link.get('jsaction')

        print(href)


getImageLinks('dog')