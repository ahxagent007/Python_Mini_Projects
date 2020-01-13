from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        some_json = request.get_json()
        return jsonify({'you sent' : some_json}), 201
    else:

        return jsonify({"code" : getLinksYoutube('Nahid')})

@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result' : num*10})


@app.route('/YT/<search_text>', methods=['GET'])
def getLinksYoutube(search_text):
    page = 1
    max_page =2

    url = "https://m.youtube.com/results?search_query="+str(search_text)

    source_code = requests.get(url)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text)
    #print(plain_text)
    allLinks = []
    i = 0
    for link in soup.findAll('a',{'class': 'yt-uix-sessionlink'}): #,{'id': 'yt-uix-sessionlink'}
        href = link.get('href')
        if(href[0:6] == '/watch'):
            #print(href)
            allLinks.append("https://www.youtube.com"+href)
            i+=1

    #print(i)
    return jsonify({"links" : allLinks, "total": str(i)})

if __name__ == '__main__':
    app.run(debug=True)

