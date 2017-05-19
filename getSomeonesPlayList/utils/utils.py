def getUrlsId(url):
    id = url.split('id')
    if len(id) < 1:
        return None;
    return id[1].split('=')[1]