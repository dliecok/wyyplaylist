from pymysql import IntegrityError
from selenium import webdriver

# browser = webdriver.Chrome("./chromedriver")
from getSomeonesPlayList import getList, sqlOperate
from getSomeonesPlayList.utils import utils

browser = webdriver.PhantomJS(executable_path="/apps/run/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
browser.get('http://music.163.com/user/home?id=346110970')

browser.switch_to.frame('g_iframe')

lis = browser.find_element_by_id('cBox').find_elements_by_class_name('msk')

srcList = set();

for a in lis:
    url = a.get_attribute('href')
    srcList.add(url)

    id = utils.getUrlsId(url)
    fadf = getList.makeASongs(id)

    for sinfo in fadf:
        values = list()

        values.append('"' + sinfo.sId + '"')
        nname = str(sinfo.sName).replace("\"", "'")
        values.append('"' + nname + '"')
        values.append('"' + sinfo.sUrl + '"')
        values.append('"' + id + '"')

        # klist = sorted(sinfo.__dict__.items(), key=lambda d:d[0])
        # for (k,v) in klist:
        #     val = str(v)
        #     val = '"' + val + '"'
        #     values.append(val)

        sqlStr = "insert into songs_info (s_id, s_name, s_url, s_list_id) values (" + ','.join(values) + ")"
        print(sqlStr)
        try:
            sqlOperate.query(sqlStr)
        except IntegrityError as e:
            print("duplicate key-")
            continue

browser.close()