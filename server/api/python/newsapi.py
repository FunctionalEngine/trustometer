from bs4 import BeautifulSoup
from pprint import pprint
import urllib.request
import re
import requests
import json

def get_news(keywords):
    keyword = 'q='+re.sub(r"\s+", ' ', keywords)+'&'
    url = ('https://newsapi.org/v2/everything?'+keyword+'from=2018-10-01&sortBy=popularity&apiKey=0484edc4a86c472a8b0ae8b4a4205f42')
    res = (requests.get(url)).json()["articles"]
    newsTitles = []
    for news in res:
        newsTitles.append((news["title"]+".").lower())
    return newsTitles