#最简单的爬取网页代码

import re
import urllib.request
url = 'http://crh19970307.github.io/blog/'
webPage=urllib.request.urlopen(url)
data = webPage.read()
data = data.decode('gbk', 'ignore').encode("UTF-8")
#由于Windows默认为GBK，因此若直接用UTF8输出会报错
#data=data.decode('UTF-8') 在IDE里面采用这种方法
print(data)

#print(type(webPage))
#print(webPage.geturl())
#print(webPage.info())
#print(webPage.getcode())