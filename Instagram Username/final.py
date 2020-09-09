import requests
import threading
import time
import itertools
import random
import ctypes  # An included library with Python install.   
from instagram_private_api import Client

try:
    client_data = open('Account.txt','r').read().split('\n')
    user_name = client_data[0].split("= '")[1][:-1]
    password = client_data[1].split("= '")[1][:-1]
except:
    print('Please Enter Username and Password in Account.txt')
    exit(0)

PROXY = True

all_proxies = [i for i in open('proxy_list.txt','r').read().split('\n') if len(i)>1]
STATE = True

API = None
PARAMS = None
FRST = 1
try:
    API = Client(user_name, password,authenticate=True)
    current_user_data = API.current_user()['user']
    PARAMS = {
            'username': '',
            'gender': current_user_data['gender'],
            'phone_number': current_user_data['phone_number'],
            'first_name': 'Vnes',#current_user_data['full_name'],
            'biography': current_user_data['biography'],
            'external_url': current_user_data['external_url'],
            'email': current_user_data['email'],
        }
except:
    ctypes.windll.user32.MessageBoxW(0, 'Loging Error', "Wrong Credentials", 1)
    exit(0)
print('!!Login Successfully!!')

def change_username(newusername):
    global API,PARAMS,FRST
    PARAMS['username']=newusername
    if FRST:
        FRST = 0
        try:
            PARAMS.update(API.authenticated_params)
            r=API._call_api('accounts/edit_profile/',params=PARAMS)
            if r['status']=='ok':
                data = 'New Username ->  @{}'.format(newusername)
                ctypes.windll.user32.MessageBoxW(0, data, "User Changed", 1)
                exit(0)
            else:
                ctypes.windll.user32.MessageBoxW(0, str(r), "User Changed", 1)
                exit(0)
        except:
            for tries in range(5):
                try:
                    API = Client(user_name, password,authenticate=True)
                    PARAMS.update(API.authenticated_params)
                    r=API._call_api('accounts/edit_profile/',params=PARAMS)
                    if r['status']=='ok':
                        data = 'New :  @'.format(newusername)
                        ctypes.windll.user32.MessageBoxW(0, data, "User Changed", 1)
                        exit(0)
                    else:
                        ctypes.windll.user32.MessageBoxW(0, str(r), "User Changed", 1)
                        exit(0)
                except:
                    print('{} Trying Login Again and Changeing Username to @()'.format(tries,username))
            ctypes.windll.user32.MessageBoxW(0, "Some Error Occured", "User Changed", 1)
    else:
        print('Already Changing')
    

def get_headers():
    global all_proxies,PROXY,STATE
    url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
    while STATE:
        try:
            if not STATE:
                break
            r = requests.head(url,proxies={"https": random.choice(all_proxies)})
            cookies = r.cookies
            csrf_token = cookies['csrftoken']
            mid = cookies['mid']
            headers = {
            'User-Agent': 'Instagram 128.0.0.26.128 Android (26/8.0.0; 480dpi; 1080x1920; HUAWEI/HONOR; STF-L09; HWSTF; hi3660; ru_RU; 124584015)',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-CSRFToken': csrf_token,
            'Cookie': 'csrftoken={}; mid={}'.format(csrf_token,mid)

            }
            return headers
        except:
            pass

def check_username(usernames):
    global all_proxies,PROXY,STATE
    headers=get_headers()
    r = None
    while STATE:
        for username in usernames:
            if not STATE:
                break
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            data = {'email': 'mdmr.emailwork'+username+'21@gmail.com','password': 'GoogleWrodl17234@@#','username':username}#its fake data yah i see
            while STATE:
                if not STATE:
                    break
                try:
                    if PROXY:
                        r = requests.post(url,headers=headers,data=data,proxies={"https": random.choice(all_proxies)})
                    else:
                        r = requests.post(url,headers=headers,data=data)
                    if r.status_code!=200:
                        headers=get_headers()
                        continue
                    else:
                        break
                except:
                    headers=get_headers()

            
            try:
                data = r.json()
                if 'errors' in data.keys():
                    print(username,' =>',data['errors'],end='\n')
                else:
                    try:
                        if data['dryrun_passed']:
                            STATE = False
                            print('Username is found @'+username)
                            change_username(username)
                            #ctypes.windll.user32.MessageBoxW(0, 'Username is found @'+username, "User found", 1)
                            break
                        else:
                            print(data)
                    except:
                        pass
            except:
                pass
            
            


'''target_users = [i for i in open('list.txt','r').read().split('\n') if len(i)>1]
check_username(target_users)'''

def get_usernames():
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

no_thread = 50
total_users = len(target_users)
thread_per_data = total_users//no_thread



if thread_per_data>2:
    thread=[]
    for th in range(no_thread):
        target_userss = target_users[th*thread_per_data:(th+1)*thread_per_data]
        th = threading.Thread(target=check_username,args=(target_userss,))
        th.start()
        thread.append(th)

    for ii in thread:
        ii.join()
        
else:
    check_username(target_users)
