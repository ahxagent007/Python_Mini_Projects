import json
import random
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

#649/28232/

def test(id, season):
    url = 'https://www.sofascore.com/u-tournament/' + str(id) + '/season/' + str(season) + '/json'
    proxies = get_free_proxies()
    for proxy in proxies:
        session = requests.Session()
        session.proxies = {"http": proxy, "https": proxy}
        try:
            data = session.get(url, timeout=5).text

            if len(data) > 15000:
                return jsonify({'message': "success", 'status': 1, 'data':data})
                break

        except Exception as e:
            print(e)
            continue

    return jsonify({'message': "not found", 'status': 2, 'data': []})

def xian(id, season):
    url = 'https://www.sofascore.com/u-tournament/' + str(id) + '/season/' + str(season) + '/json'

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    print(soup.text)

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies

def get_session(proxies):
    # construct an HTTP session
    session = requests.Session()
    # choose one random proxy
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session


def xian2(id, season):
    url = 'https://www.sofascore.com/u-tournament/' + str(id) + '/season/' + str(season) + '/json'

    proxies = get_free_proxies()

    s = get_session(proxies)
    page = s.get(url, timeout=1.5)
    #soup = BeautifulSoup(page.text, 'html.parser')

    print(page)

'''for i in range(20):
    s = get_session(proxies)
    try:
        print("Request page with IP:", s.get(url, timeout=2).text)
    except Exception as e:
        print(e)
        continue'''

#xian2(649, 28232)
url = 'https://www.sofascore.com/u-tournament/649/season/28232/json'
#url = 'http://icanhazip.com'
proxies = get_free_proxies()
print('Prixy Size : '+str(len(proxies)))
#goodProxy = ['147.135.7.123:3128', '54.38.155.89:6582', '193.233.137.115:8080', '13.75.77.214:44355', '75.150.251.146:3128', '95.174.67.50:18080', '83.97.23.90:18080', '104.45.188.43:3128', '64.71.145.122:3128', '81.201.60.130:80', '43.224.8.121:6666', '178.168.114.122:8080', '36.79.189.15:8080', '91.135.148.198:51498', '139.99.105.5:80', '46.218.155.194:3128', '110.168.212.55:8080', '62.99.67.216:8080', '145.239.121.218:3129', '103.113.17.102:8080', '104.41.54.53:3128', '188.165.16.230:3129', '41.217.219.53:31398', '125.26.120.237:8080', '36.92.94.50:8080']
#goodProxyless2 = ['95.174.67.50:18080', '83.97.23.90:18080', '104.45.188.43:3128', '139.99.105.5:80', '46.218.155.194:3128', '145.239.121.218:3129', '104.41.54.53:3128', '188.165.16.230:3129', '125.26.120.237:8080', '36.92.94.50:8080']
#betterProxy = []

for proxy in proxies:
    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}
    try:
        asd = session.get(url, timeout=5).text
        print("Request page with proxy IP:", asd)
        #goodProxy.append(proxy)
        #betterProxy.append(proxy)
        if len(asd) > 15000:
            break

    except Exception as e:
        print(e)
        continue
# error 11352
# data 144618
#print(betterProxy)

'''f = open("proxies.txt", "w")
for p in goodProxyless2:
    f.write(p+'\n')
f.close()'''



