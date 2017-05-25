#coding=utf-8
#urllib模块提供了读取Web页面数据的接口
import urllib
#re模块主要包含了正则表达式
import re

import datetime

def getdatestr():
    begin = datetime.date(2017,2,1)
    end = datetime.date(2017,3,31)
    d = begin  
    delta = datetime.timedelta(days=1)  
    while d <= end:
        #Linux
        #mydatetime.strftime('%-m/%d/%Y %-I:%M%p')
        # Windows
        #mydatetime.strftime('%#m/%d/%Y %#I:%M%p')
        #https://bingwallpaper.com/CN/20170522.html
        url="https://bingwallpaper.com/CN/"+d.strftime("%Y%m%d")+".html"
        #url="http://www.istartedsomething.com/bingimages/?m="+d.strftime("%#m")+"&y="+d.strftime("%Y")+"#"+d.strftime("%Y%m%d")+"-cn"
        print url
        html = getHtml(url)
        print getImg(html,d)
        d += delta

#定义一个getHtml()函数
def getHtml(url):
    page = urllib.urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    html = page.read() #read()方法用于读取URL上的数据
    #print html
    return html

def getImg(html,d):
    #reg = r'src="(.+?\.jpg)"'    #正则表达式，得到图片地址
    #reg = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+.jpg'
    reg = r'www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+.jpg'
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名

    for imgurl in imglist:
        #http://www.bing.com/az/hprichbg/rb/QueensParkGlasshouse_ZH-CN11893975642_1366x768.jpg
        #print imgurl
        imgurl1080=imgurl.replace('1366','1920').replace('768','1080')
        httpurl='http://'+imgurl1080
        # httpurl='http://'+imgurl
        print httpurl
        urllib.urlretrieve(httpurl,'G:\Mark\Spider\%s.jpg' % d.strftime("%Y%m%d"))
        
getdatestr()
