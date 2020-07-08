from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://raw.githubusercontent.com/leopheard/InstituteForJustice/master/resources/lib/I4Jfeed.xml"
url2 = "http://feeds.soundcloud.com/users/soundcloud:users:84493247/sounds.rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/f7/02/ec/f702ecc0-af82-33fa-13b4-ca7b7f3f404c/mza_150107582849176952.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/f7/02/ec/f702ecc0-af82-33fa-13b4-ca7b7f3f404c/mza_150107582849176952.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://is4-ssl.mzstatic.com/image/thumb/Podcasts123/v4/68/6d/e4/686de4f8-c960-3546-030e-007ea6a616e9/mza_8205412303251836831.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://is4-ssl.mzstatic.com/image/thumb/Podcasts123/v4/68/6d/e4/686de4f8-c960-3546-030e-007ea6a616e9/mza_8205412303251836831.jpg/600x600bb.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup2)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items


if __name__ == '__main__':
    plugin.run()
