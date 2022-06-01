

import urllib3
from bs4 import BeautifulSoup
import requests
import json


def content(url_input):
    http = urllib3.PoolManager()
    response = http.request('GET', url_input)
    soup = BeautifulSoup(response.data, features="lxml")
    soup.prettify()
    datas = soup.find_all("body")

    for data in datas:
        res = json.loads(data.text)

    a = res.get('dependencies')
    b = a.get('axios')
    c = b.split('^')

    d = ""+c[1]

    return d
