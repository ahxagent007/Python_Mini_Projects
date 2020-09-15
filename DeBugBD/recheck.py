from flask import Flask, jsonify
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import threading

app = Flask(__name__)


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


@app.route('/')
def index():
    return 'XIAN'


def test(id, season):
    url = 'https://www.sofascore.com/u-tournament/' + str(id) + '/season/' + str(season) + '/json'
    proxies = get_free_proxies()
    # goodProxy = ['147.135.7.123:3128', '54.38.155.89:6582', '193.233.137.115:8080', '13.75.77.214:44355', '75.150.251.146:3128', '95.174.67.50:18080', '83.97.23.90:18080', '104.45.188.43:3128', '64.71.145.122:3128', '81.201.60.130:80', '43.224.8.121:6666', '178.168.114.122:8080', '36.79.189.15:8080', '91.135.148.198:51498', '139.99.105.5:80', '46.218.155.194:3128', '110.168.212.55:8080', '62.99.67.216:8080', '145.239.121.218:3129', '103.113.17.102:8080', '104.41.54.53:3128', '188.165.16.230:3129', '41.217.219.53:31398', '125.26.120.237:8080', '36.92.94.50:8080']
    # return jsonify({'message': "success", 'status': 'XIAN', 'data':proxies})
    exceptionCount = 0
    exceptionsList = []
    for proxy in proxies:
        session = requests.Session()

        session.proxies = {
            "http": proxy,
            "https": proxy
        }

        try:
            data = session.get(url, timeout=1.5).text

            if len(data) > 15000:
                return jsonify({'message': "success", 'status': 1, 'data': data, 'serial': exceptionCount})
                break

        except Exception as e:
            # print(e)
            exceptionCount = exceptionCount + 1
            exceptionsList.append(e)
            # return jsonify({'message': "not found", 'status': 'XIAN', 'data': str(e), 'EXCEPTOIN': exceptionCount})
            continue

    return jsonify({'message': "not found", 'status': 2, 'data': exceptionsList, 'EXCEPTOIN': exceptionCount})


@app.route('/test/<id>/<season>/')
def test2(id, season):
    url = 'https://www.sofascore.com/u-tournament/' + str(id) + '/season/' + str(season) + '/json'
    proxies = get_free_proxies()

    try:
        distance = int(len(proxies) / 10)
        x1 = threading.Thread(target=thd, args=(proxies[:distance], url, 'T1'))
        x2 = threading.Thread(target=thd, args=(proxies[distance:distance * 2], url, 'T2'))
        x3 = threading.Thread(target=thd, args=(proxies[distance * 2:distance * 3], url, 'T3'))
        x4 = threading.Thread(target=thd, args=(proxies[distance * 3:distance * 4], url, 'T4'))
        x5 = threading.Thread(target=thd, args=(proxies[distance * 4:distance * 5], url, 'T5'))
        x6 = threading.Thread(target=thd, args=(proxies[distance * 5:distance * 6], url, 'T6'))
        x7 = threading.Thread(target=thd, args=(proxies[distance * 6:distance * 7], url, 'T7'))
        x8 = threading.Thread(target=thd, args=(proxies[distance * 7:distance * 8], url, 'T8'))
        x9 = threading.Thread(target=thd, args=(proxies[distance * 8:distance * 9], url, 'T9'))
        x0 = threading.Thread(target=thd, args=(proxies[distance * 9:], url, 'T0'))

        x1.start()
        x2.start()
        x3.start()
        x4.start()
        x5.start()
        x6.start()
        x7.start()
        x8.start()
        x9.start()
        x0.start()

        x1.join()

    except Exception as e:
        # print("Error: unable to start thread : "+str(e))
        return jsonify({'message': "Error: unable to start thread : " + str(e), 'status': 'XIAN', 'data': []})

    return jsonify({'message': "not found", 'status': 2, 'data': []})


def thd(proxies, url, name):
    for proxy in proxies:
        session = requests.Session()
        session.proxies = {"http": proxy, "https": proxy}
        try:
            data = session.get(url, timeout=5).text

            if len(data) > 15000:
                return jsonify({'message': "success", 'status': 1, 'data': data, 'serial': name})
                break

        except Exception as e:
            # print(name+' : '+str(e))
            continue


@app.route('/football/<date>/')
def football_list(date):
    url = 'https://www.sofascore.com/football//' + date + '/json'
    try:
        data = json.loads(urlopen(url).read().decode("utf-8"))
        return jsonify({'message': "success", 'status': 1, 'data': data})
    except:
        return jsonify({'message': "not found", 'status': 2, 'data': []})


@app.route('/lineups/<num>/')
def linesups_json(num):
    url = 'https://api.sofascore.com/api/v1/event/' + num + '/lineups'
    try:
        data = json.loads(urlopen(url).read().decode("utf-8"))
        return jsonify({'message': "success", 'status': 1, 'data': data})
    except:
        return jsonify({'message': "not found", 'status': 2, 'data': []})


@app.route('/incidents/<num>/')
def incidents_json(num):
    url = 'https://api.sofascore.com/api/v1/event/' + num + '/incidents'
    try:
        data = json.loads(urlopen(url).read().decode("utf-8"))
        return jsonify({'message': "success", 'status': 1, 'data': data})
    except:
        return jsonify({'message': "not found", 'status': 2, 'data': []})


@app.route('/players/<num>/')
def players_json(num):
    # 24156/
    url = 'https://api.sofascore.com/api/v1/team/' + num + '/players'
    try:
        data = json.loads(urlopen(url).read().decode("utf-8"))
        return jsonify({'message': "success", 'status': 1, 'data': data})
    except:
        return jsonify({'message': "not found", 'status': 2, 'data': []})


if __name__ == '__main__':
    app.debug = False
    app.run()