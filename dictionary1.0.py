#���ý�ɽ�ʵ䷭�룬���ɵ�������ʽ�ʵ䣬��exit�˳�
import urllib.request
import socket
import re
import sys
import os
def saveFile(data):
    save_path = "G:\Program Design\\python\\������ϰ\\data\\tmp.out"
    f_obj = open(save_path, 'wb') # wb ��ʾ�򿪷�ʽ
    f_obj.write(data)
    f_obj.close()
weburl = 'http://www.iciba.com/'
webheader1 = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
webheader2 = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    #'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.iciba.com',
    'DNT': '1'
    }
while True:
    add= input("input:")
    if add=='exit':break
    weburl = 'http://www.iciba.com/'
    weburl = weburl+ add
    req = urllib.request.Request(url=weburl, headers=webheader2)
    webPage = urllib.request.urlopen(req)  #��������ͷ
    contentBytes = webPage.read()
    #contentBytes=contentBytes.decode('utf-8')
    #saveFile(data)
    #print(contentBytes)
    #print(re.findall(r'<span.+?</span>', str(contentBytes)))
    for i in re.findall(r'<span class="prop".+?clearfix', str(contentBytes)):

        for j in re.findall(r'<span>.+?</span>', i):
            #j= unicode(j, "ascii")
            print (str.encode(j))#���뻷�ڳ�������
    #data = data.decode('UTF-8')
    #print(data)

