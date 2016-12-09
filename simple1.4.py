#提取出一个网页的图片，并下载
#下载的是虫部落里的图标文件

import urllib.request
import socket
import re
import sys
import os
targetDir = 'G:\Program Design\\python\\爬虫练习\\data2'  #文件保存路径
def destFile(path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/') #图片URL里的/最后一次出现的位置
    t = os.path.join(targetDir, path[pos+1:])#将本地路径与图片URL最后部分连接起来
    return t
if __name__ == '__main__':  #程序运行入口
    weburl = 'http://so.chongbuluo.com/'
    webheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=weburl, headers=webheaders)  #构造请求报头
    webPage = urllib.request.urlopen(req)  #发送请求报头
    contentBytes = webPage.read()
    #contentBytes=contentBytes.decode('UTF-8')
   # data = contentBytes
    #data=data.decode('UTF-8')
    #print (data)
   # print( re.findall(r'src="http://(.*).jpg"', str(contentBytes)) )
    print(str(contentBytes))
    print(re.findall(r'src="(.+?\.ico)"', str(contentBytes)))#正则表达式不太好写
for link in set(re.findall(r'src="(.+?\.ico)"', str(contentBytes)) ) : #正则表达式查找所有的图片，刚开始是用的for link,t in...报错，后来改成一个link就好了
        print(link)
        try:
            urllib.request.urlretrieve(link, destFile(link)) #下载图片
        except:
            print('失败') #异常抛出
   # urllib.request.urlretrieve('http://gg.qwghq.com/images/nav_logo242_hr.png', destFile('http://gg.qwghq.com/images/nav_logo242_hr.png'))



