#coding=utf-8
import datetime
import urllib
#print datetime.date(2017,1,1).strftime('%Y%#m:%#d')
#urllib.urlretrieve('http://www.bing.com/az/hprichbg/rb/QueensParkGlasshouse_ZH-CN11893975642_1366x768.jpg','G:\Mark\Spider\my.jpg')
url='http://'+'www.bing.com/az/hprichbg/rb/QueensParkGlasshouse_ZH-CN11893975642_1366x768.jpg'
print url
urllib.urlretrieve(url,'G:\Mark\Spider\my.jpg')
