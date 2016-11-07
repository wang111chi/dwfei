#!-*- coding:utf-8 -*-
__author__ = 'Administrator'
import requests
import urllib2
import urllib
url='http://www.cathaypacific.com/cx/sc_CN.html'

def query_fare():
    url2='https://book.cathaypacific.com/pl/CathayPacificV2/wds/OverrideServlet?WDS_JS_TRACE_OFF'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36','Referer':'http://www.cathaypacific.com/wdsibe/IBEFacade'}
    name={
    "round-trip":'O', #'O'单程   'R'往返
    "depart-label":u'广州, (CAN)',#出发地data-url="/cx/sc_CN.ibe-od.sc.true.REV.0.searchOption.origin.json"
    "destination-label":u'曼谷, (BKK)',#目的地ata-url="/cx/sc_CN.ibe-od.sc.true.REV.0.searchOption.destination.json"
    "flexible-dates":'20160611',
    "cabin-class":'Y',#头等舱F, 公务舱C, 特选经济舱W, 经济舱Y
    "passenger-adults":'2',#1,2,3,4,5,6
    "passenger-children":'1',#0,1,2,3,4,5
    "passenger-infants":'0',#0,1,2
    }
    data = urllib.urlencode(name)
    request = urllib2.Request(url2,data, headers)
    response = urllib2.urlopen(request)
    page = response.read()
    return page

def select_datetime():
    name="FLIGHT_ID_1"
    value="1"
    return name

def persion_info():
    url='https://book.cathaypacific.com/pl/CathayPacificV2/wds/AddElementsServlet;jsessionid=D9Q91UlY93HC8RBXy61An61bfHy38X5L-bi43Xx_uVJ0jvn8RfBS!-2111023288!50321411'
    headers = {
    #"DNT":'1',
    #"Host":"book.cathaypacific.com",
    #"Origin":"https://book.cathaypacific.com",
    "Referer":"https//book.cathaypacific.com/pl/CathayPacificV2/wds/OverrideServlet;jsessionid=D9Q91UlY93HC8RBXy61An61bfHy38X5L-bi43Xx_uVJ0jvn8RfBS!-2111023288!50321411",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    }
    info={"SELECT_TITLE_1":"MR",#MR,MRS,MS,MISS,DR,PROF
          "LAST_NAME_1":"wan",
          "FIRST_NAME_1":"wanchi",
          "CONTACT_POINT_EMAIL_1":"15671532758@163.com",
          "PHONE_COUNTRY":"86",
          "PHONE_AREA":"",
          "PHONE_NUMBER":"18565441226"
          }
    data = urllib.urlencode(info)
    request = urllib2.Request(url,data, headers)
    response = urllib2.urlopen(request)
    page = response.read()
    return page

if __name__=='__main__':
    #pg1=query_fare() #req=requests.post(url2,json=name)
    #print pg1
    r=persion_info()
    print r







