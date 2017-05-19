import requests
from bs4 import BeautifulSoup

from getSomeonesPlayList.model.SongInfo import SongInfo
from getSomeonesPlayList.utils import utils

headers = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

prefix = 'http://music.163.com'

def makeASongs(listId):
    play_url = prefix + '/playlist?id=' + listId

    s = requests.session()

    s = s.get(play_url, headers=headers).content

    s = BeautifulSoup(s)

    main = s.find('ul', {'class': 'f-hide'})

    newsongs = set()
    for music in main.findAll('a'):
        url = music['href'];

        id = utils.getUrlsId(url)

        temp = SongInfo(id, music.text, prefix + url)

        newsongs.add(temp)

    return newsongs
