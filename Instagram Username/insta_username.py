import aiohttp, asyncio

import requests
from PyQt5.QtCore import *
import itertools

class Checker(QThread):

    #Signal Variables.
    update = pyqtSignal(object)
    pupdate = pyqtSignal(object)
    count = 0

    #Global Variables.
    LOGIN_URL = 'https://www.instagram.com/accounts/login/ajax/'
    URL = 'https://www.instagram.com/{}'

    def __init__(self, igname, igpass):
        super().__init__()
        self.igname = igname
        self.igpass = igpass

        print('__init__')
    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(self.main())
        finally:
            loop.close()

    #Checks username availability.
    async def check_usernames(self, username, sem, session, lock):
        async with sem:
            try:
                async with session.get(self.URL.format(username)) as resp:
                    text = await resp.text()
                    if "Page Not Found" in text:
                        self.update.emit(username)
                        print('UNIQUE '+username)
                    else:
                        print('not unique')

            except:
                pass

            finally:
                with await lock:
                    self.count += 1
                self.pupdate.emit(self.count)

    #Creates a task for each username and then runs each task.
    async def main(self):
        sem = asyncio.BoundedSemaphore(50)
        lock = asyncio.Lock()
        async with aiohttp.ClientSession() as session:
            cont = await self.login(self.igname, self.igpass, session)
            if cont:
                usernames = get_usernames()
                tasks = [self.check_usernames(username, sem, session, lock) for username in usernames]
                await asyncio.gather(*tasks)
                print('main')
            else:
                pass

    #Logs into Instagram.
    async def login(self, username, password, session):
        async with session.get(self.URL.format('')) as response:
            csrftoken = await response.text()

        csrftoken = csrftoken.split('csrf_token":"')[1].split('"')[0]

        async with session.post(
                self.LOGIN_URL,
                    headers={
                        'x-csrftoken': csrftoken, 'x-instagram-ajax':'1',
                        'x-requested-with': 'XMLHttpRequest',
                        'Origin': self.URL, 'Referer': self.URL
                        },
                    data={
                        'username':username, 'password':password
                    }
                ) as response:

                text = await response.json()

                if text['authenticated']:
                    return True
                else:
                    self.update.emit('Login Failed')
                    return False


def get_usernames1():
    s = 'abcdefghijklmnopqrstuvwxyz._0123456789'

    user_names4 = list(itertools.permutations(s, 4))
    user_names3 = list(itertools.permutations(s, 3))
    user_names2 = list(itertools.permutations(s, 2))
    user_names1 = list(itertools.permutations(s, 1))

    lst4 = []
    lst3 = []
    lst2 = []
    lst1 = []

    for s in user_names4:
        lst4.append("".join(s))

    for s in user_names3:
        lst3.append("".join(s))

    for s in user_names2:
        lst2.append("".join(s))

    for s in user_names1:
        lst1.append("".join(s))

    return lst1 + lst2 + lst3 + lst4

def get_usernames():
    f = open('output.txt', 'r')
    user_names = []
    for s in f:
        user_names.append(s)
    return user_names

def createAccount(ig_email, ig_username, ig_password, ig_firstname):
    ########## ACCOUNT CONFIG ##########
    '''ig_email = 'your@email.com'
    ig_username = 'username'
    ig_password = 'password'
    ig_firstname = 'firstname'''
    ########## ACCOUNT CONFIG ##########

    url = "https://www.instagram.com/accounts/web_create_ajax/"
    headers = {
        'accept': "*/*",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "es-ES,es;q=0.9,en;q=0.8",
        'content-length': "241",
        'origin': "https://www.instagram.com",
        'referer': "https://www.instagram.com/",
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
        'x-csrftoken': "95RsiHDyX9J6AcVz9jtCIySbwf75QhvG",
        'x-instagram-ajax': "c7e210fa2eb7",
        'x-requested-with': "XMLHttpRequest",
        'Cache-Control': "no-cache"
    }

    payload = {
        'email': ig_email,
        'password': ig_password,
        'username': ig_username,
        'first_name': ig_firstname,
        'client_id': 'W6mHTAAEAAHsVu2N0wGEChTQpTfn',
        'seamless_login_enabled': '1',
        'gdpr_s': '%5B0%2C2%2C0%2Cnull%5D',
        'tos_version': 'eu',
        'opt_into_one_tap': 'false'
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

igname = 'secret_developers'
igpass = 'XiAn2011'

thread = Checker(igname, igpass)
thread.start()

#createAccount('asdawqe654@gmail.com','asdawqe654', 'PassWOrd!@#123', 'Eklash')
