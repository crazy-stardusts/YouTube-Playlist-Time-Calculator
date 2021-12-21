from urllib import request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

if __name__ == "__main__":
    urll = 'https://www.youtube.com/playlist?list=PLpuxPG4TUOR619ThKfb5zMit6fWMbHvIt'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

    req = requests.get(urll, headers = headers)

    soup = BeautifulSoup(req.content, 'html5lib')
    #print(soup.prettify())


    data = soup.findAll("script")
    #print(data[31])
    data = data[31]
    
    dt = data.text
    file = open('view.txt','w')
    file.write(dt)


        