#将抓取到的网页内容保存起来

import urllib.request

def saveFile(data):
    save_path = 'G:\Program Design\\python\\爬虫练习\\data\\tmp.out'
    f_obj = open(save_path, 'wb') # wb 表示打开方式
    f_obj.write(data)
    f_obj.close()
    ##注意！这里最开始用的路径是G:\temp.out，始终报错，是因为\t连在了一起
    ##在路径中除了第一个之\外，\都要用\\代替，否则也会报错
    
weburl = 'http://www.douban.com/'
webheader1 = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
webheader2 = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    #'Accept-Encoding': 'gzip, deflate',
    'Host':  'www.douban.com',
    'DNT': '1'
    }
req = urllib.request.Request(url=weburl, headers=webheader2)
webPage=urllib.request.urlopen(req)
data = webPage.read()
#先将data保存，然后再进行解码，否则无法保存
saveFile(data)# 将data变量保存到目录下
data = data.decode('UTF-8')
print(data)
#print(type(webPage))
#print(webPage.geturl())
#print(webPage.info())
#print(webPage.getcode())