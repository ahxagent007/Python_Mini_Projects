import json
import threading
import time
from threading import Timer
import requests
from bs4 import BeautifulSoup

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

def test(id, season, sofa_api):
    print('Getting Time ^^^^^^^^^^^^^^^^^^^^^^ ')
    url = 'https://www.sofascore.com/u-tournament/' + str(id) + '/season/' + str(season) + '/json'
    print(url)
    proxies = get_free_proxies()

    i = 0
    for proxy in proxies:
        i+=1
        x = threading.Thread(target=fast_run, args=(proxy, sofa_api, i, url))
        x.start()

    #return jsonify({'message': "not found", 'status': 2, 'data': []})

def fast_run(proxy, sofa_api, i, url):
    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}
    print('THREADING : : : ' + str(sofa_api) + ' #' + str(i) + ' : Time ' + proxy)
    try:
        data = session.get(url).text
        print(data)
        print(len(data))

        try:
            data = json.loads(data)
            # statusDescription = data['tournamentInfo']['featuredMatches']['tournaments'][0]['events'][0][
            #    'statusDescription']
            # print(statusDescription)
            found = False
            statusDescription = 'FT'
            for e in data['tournamentInfo']['featuredMatches']['tournaments'][0]['events']:
                if e['id'] == sofa_api:
                    statusDescription = e['statusDescription']
                    found = True
                    break
            if not found:
                for e in data['events']['roundMatches']['tournaments'][0]['events']:
                    if e['id'] == sofa_api:
                        statusDescription = e['statusDescription']
                        found = True
                        break
            if not found:
                for t in data['events']['weekMatches']['tournaments']:
                    for e in t['events']:
                        if e['id'] == sofa_api:
                            statusDescription = e['statusDescription']
                            found = True
                            break

            if (not found):
                print('statusDescription NOT FOUND')

            else:
                print('>>>>>>>>>' + str(sofa_api) + ' ' + str(statusDescription) + '<<<<<<<<<<<<<')
            # return statusDescription
            incidents(sofa_api, statusDescription, proxy)


        except Exception as e2:
            print('NOT JSON : ' + str(e2))


    except Exception as e:
        print(str(e))


def incidents(sofa_api, statusDescription, proxy):
    print('Getting Incidents $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    url = 'https://api.sofascore.com/api/v1/event/'+str(sofa_api)+'/incidents'
    print(url)
    print('incidents '+proxy)

    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}

    try:
        data = session.get(url).text
        print(data)
        print(len(data))

        try:
            data1 = json.loads(data)
            if data1['error']['code'] == 404:
                #return None
                lineup(sofa_api, statusDescription, proxy, None)
            else:
                #return data
                lineup(sofa_api, statusDescription, proxy, data)
        except Exception as e2:
            print('NOT JSON : ' + str(e2))
            lineup(sofa_api, statusDescription, proxy, data)

    except Exception as e:
        print(str(e))
        lineup(sofa_api, statusDescription, proxy, None)


def lineup(sofa_api, statusDescription, proxy, incidents):
    print('Getting Lineup ***************************')
    url = 'https://api.sofascore.com/api/v1/event/'+str(sofa_api)+'/lineups'
    print(url)
    print('Lineup '+proxy)

    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}
    try:
        data = session.get(url).text
        print(data)
        print(len(data))

        send_data(sofa_api, statusDescription, incidents, data)

    except Exception as e:
        print(str(e))



def send_data(sofa_api, time, incident, lineup):
    print('Sending data to server ..................')
    # api-endpoint
    URL = "http://teamplan.mydbdsoft.com/api/football/update-sofa-data"
    print(URL)

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'sofa_api': sofa_api, 'time': time, 'incident': incident, 'lineup': lineup}
    print(PARAMS)

    # sending get request and saving the response as response object
    r = requests.post(url=URL, data=PARAMS)

    # extracting data in json format
    data = r.text

    print('Reply from API : '+str(data))
    print('END THREADING-------------------------------------------------------------------------------------------------------------------------------')

def get_details():
    url = 'http://teamplan.mydbdsoft.com/api/football/live-matches-list'

    session = requests.Session()
    try:
        data = session.get(url, timeout=5).text

        print(data)
        return data

    except Exception as e:
        print(str(e))

def start_process():
    print('Start THREADING -------------------------------------------------------------------------------------------------------------------------------')

    data = get_details()
    data = json.loads(data)

    for d in data:
        id_fixture = d['id_fixture']
        sofa_api = d['id_sofa_api']
        id_series = d['id_series']
        id_season = d['id_season']

        test(id_series, id_season, sofa_api)

# https://api.sofascore.com/api/v1/event/8909435/incidents
# https://www.sofascore.com/u-tournament/34/season/28222/json
# https://api.sofascore.com/api/v1/event/8909435/lineups

#start_process()

#time_sec = 60.0
#t = Timer(time_sec, start_process)
#t.start()


iteration = 1
while True:
    print('ITERATION ######## {0} ###########'.format(iteration))
    start_process()
    iteration += 1
    print('ITERATION ######## {0} ###########'.format(iteration))
    time.sleep(150.0)