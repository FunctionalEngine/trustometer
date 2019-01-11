from bs4 import BeautifulSoup
import urllib.request
import json
import sys

def get_target_title(url, level):
    html = get_url(url)
    titles = parse_titles(html, level)
    return titles

def get_url(url):
    with urllib.request.urlopen(url) as response:
        page = response.read()
    return BeautifulSoup(page, 'html.parser')

def parse_titles(html, maxdepth):
        titles = []

        for i in range (maxdepth):
            titles.append('h' + str(i))

        list_titles = html.find_all(titles)

        for i in range (len(list_titles)):
            list_titles[i] = list_titles[i].get_text().strip()

        #return json.dumps(list_titles, ensure_ascii=False).encode('utf-8')
        return list_titles