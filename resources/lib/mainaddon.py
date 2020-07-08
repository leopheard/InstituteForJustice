import requests
import re
from bs4 import BeautifulSoup

url1 = "https://ij.org/feed/bound-by-oath/"
url2 = "http://feeds.soundcloud.com/users/soundcloud:users:84493247/sounds.rss"

def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
get_soup1("https://ij.org/feed/bound-by-oath/")
def get_soup2(url2):
    page = requests.get(url2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup2))
    return soup2
get_soup2("http://feeds.soundcloud.com/users/soundcloud:users:84493247/sounds.rss")

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item', limit=12):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/f7/02/ec/f702ecc0-af82-33fa-13b4-ca7b7f3f404c/mza_150107582849176952.jpg/600x600bb.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/f7/02/ec/f702ecc0-af82-33fa-13b4-ca7b7f3f404c/mza_150107582849176952.jpg/600x600bb.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast2(soup2):
    subjects = []
    for content in soup2.find_all('item', limit=12):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is4-ssl.mzstatic.com/image/thumb/Podcasts123/v4/68/6d/e4/686de4f8-c960-3546-030e-007ea6a616e9/mza_8205412303251836831.jpg/600x600bb.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast2(playable_podcast2):
    items = []
    for podcast in playable_podcast2:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast3(soup2):
    subjects = []
    for content in soup2.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is4-ssl.mzstatic.com/image/thumb/Podcasts123/v4/68/6d/e4/686de4f8-c960-3546-030e-007ea6a616e9/mza_8205412303251836831.jpg/600x600bb.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast3(playable_podcast3):
    items = []
    for podcast in playable_podcast3:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
