from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)



def getLinksYoutube(search_text):
    page = 1
    max_page =2

    url = "https://www.youtube.com/results?search_query="+str(search_text)+"&sp=EgIYAQ%253D%253D"

    source_code = requests.get(url)

    plain_tex = source_code.text

    soup = BeautifulSoup(plain_tex)

    links = []

    for link in soup.findAll('a',{'id': 'video-title'}):
        href = link.get('href')
        links.append(href)

    return str(links)

    #while page < max_page:









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

if __name__ == '__main__':
    app.run(debug=True)

