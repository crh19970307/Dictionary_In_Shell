#基本功能已经实现，通过金山翻译进行爬取，得到返回页面内容，提取出翻译部分
#前一个版本主要问题在于直接将utf-8转化为str类型，提取出中文的utf-8后因为是str类型造成无法decode解码为Unicode类型，无法显示中文
#这个版本是这样解决这个问题的，将utf-8先解码为Unicode，再转化为str类型，这样就能够显示中文了，需要注意将空白字符去掉，否则会影响正则表达式

import urllib.request
import socket
import re
import sys
import os
weburl = 'http://www.iciba.com/'#金山翻译网址
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
while True:#重复输入，输入exit退出
    add= input("input:")
    if add=='exit':break
    weburl = 'http://www.iciba.com/'
    weburl = weburl+ add  #利用金山翻译特性
    req = urllib.request.Request(url=weburl, headers=webheader2)
    webPage = urllib.request.urlopen(req)  #发送请求报头
    contentBytes = webPage.read()#得到的返回内容为utf-8
    contentBytes=contentBytes.decode('utf-8')#将utf-8内容解码为Unicode
    #print(contentBytes) 测试用
    contentBytes= "".join(contentBytes.split()) #去除解码为Unicode后的空白字符，否则正则表达式会出错
    #print(contentBytes) 测试用
    #print(re.findall(r'<span>.+?</span>', str(contentBytes)))#测试用
    tag=1#用来判断是否查询到
    for i in re.findall(r'<spanclass="prop".+?clearfix', str(contentBytes)):#第一次查找，锁定单词含义分区
        #print('entered') 测试用
        for j in re.findall(r'<span>.+?</span>', i): #在分区内查找，锁定单词翻译汉语
            tag=0
            j=j[6:]
            j=j[:-7]
            if(len(j)<30):#有返回一长串，过滤掉
              print(j)#由于j中含有<span> </span>标签，将其去除掉
    if tag==1:
        print('未找到')
   
