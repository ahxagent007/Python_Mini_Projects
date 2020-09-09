from flask import Flask, jsonify
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

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


@app.route('/test/<id>/<season>/')
def test(id, season):
    url = 'https://www.sofascore.com/u-tournament/' + str(id) + '/season/' + str(season) + '/json'
    proxies = get_free_proxies()
    for proxy in proxies:
        session = requests.Session()
        session.proxies = {"http": proxy, "https": proxy}
        try:
            data = session.get(url, timeout=5).text

            if len(data) > 15000:
                return jsonify({'message': "success", 'status': 1, 'data': data})
                break

        except Exception as e:
            print(e)
            continue

    return jsonify({'message': "not found", 'status': 2, 'data': []})


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