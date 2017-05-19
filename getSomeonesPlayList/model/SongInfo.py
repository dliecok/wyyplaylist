from getSomeonesPlayList.model.baseInfo import baseInfo


class SongInfo(baseInfo):
    def __init__(self, sid, name, url):
        baseInfo.__init__(self, sid, name, **{'sUrl' : url})