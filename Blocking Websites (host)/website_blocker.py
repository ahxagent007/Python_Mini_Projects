import time
i = 0

host_path = r'C:\Windows\System32\drivers\etc\hosts'
redirected = '192.168.0.1'
website_url = ['www.facebook.com', 'www.youtube.com']

while True:
    print(i)
    i += 1
    time.sleep(1)
    with open(host_path, 'r+') as file:
        content = file.read()

        for website in website_url:
            if website in content:
                pass
            else:
                file.write(redirected+' '+website+'\n')