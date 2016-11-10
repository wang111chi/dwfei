#!-*- coding:utf-8 -*-
__author__ = 'Administrator'
import requests
import urllib2
import urllib
import re
from lxml import etree

"""
def query_fare():
    #https://book.cathaypacific.com/pl/CathayPacificV2/wds/OverrideServlet?WDS_JS_TRACE_OFF
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

    url="https://book.cathaypacific.com/pl/CathayPacificV2/wds/OverrideServlet?WDS_JS_TRACE_OFF"
    url2="https://book.cathaypacific.com/pl/CathayPacificV2/wds/FlexPricerAvailabilityServlet;jsessionid=ZDNL_0tWBgysYQN2P018Wd97Y-AI0qm7uLBE5ps9ufQZMQGqAIuY!1704511646!-1176029780"

    headers={
      "Referer":"https://book.cathaypacific.com/pl/CathayPacificV2/wds/OverrideServlet?WDS_JS_TRACE_OFF",
      "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    }
    dat={
"LANGUAGE":"CN","SITE":"CBERCBER","TRIP_FLOW":"YES","SKIN":"CX","EXTERNAL_ID":"0000PUD0Jd2bC37pDdbxqNpRHwt%3A-1","COUNTRY":"CN","FROM_SITE":"CX","B_LOCATION_2":"","B_LOCATION_1":"CAN","E_LOCATION_2":"","E_LOCATION_1":"SIN","B_DATE_1":"201611100000","B_DATE_2":"","TRAVELLER_TYPE_1":"ADT","HAS_INFANT_1":"","TRAVELLER_TYPE_2":"","HAS_INFANT_2":"","TRAVELLER_TYPE_3":"","HAS_INFANT_3":"","TRAVELLER_TYPE_4":"","HAS_INFANT_4":"","TRAVELLER_TYPE_5":"","HAS_INFANT_5":"","TRAVELLER_TYPE_6":"","HAS_INFANT_6":"","TRAVELLER_TYPE_7":"","HAS_INFANT_7":"","TRAVELLER_TYPE_8":"","HAS_INFANT_8":"","TRAVELLER_TYPE_9":"","HAS_INFANT_9":"","TRIP_TYPE":"O","COMMERCIAL_FARE_FAMILY_1":"CFFECO","COMMERCIAL_FARE_FAMILY_2":"","COMMERCIAL_FARE_FAMILY_3":"","DIRECT_NON_STOP":"","PRICING_TYPE":"I","DISPLAY_TYPE":"1","WDS_METHODS_OF_PAYMENT":"CREDITCARD","WDS_METHODS_OF_DELIVERY":"ETCKT","WDS_MOD_DESC_AIRL":"","WDS_MOD_DESC_DELIV":"","WDS_MOD_DESC_ETCKT":"e-Ticket","WDS_MOD_DESC_HAND":"","WDS_MOD_DESC_PICK":"","WDS_INCLUDE_TAX":"FALSE","WDS_PROPOSE_UPSELL":"TRUE","WDS_NEXT_CABIN":"","WDS_FROM_CALENDAR":"TRUE","FIRST_PAGE":"FFCL","PROMO_CODE":"","CALENDAR_PRICE_SELECTED":"","WDS_DATE":"201611100000"}
    dat2={"LANGUAGE":"CN","SITE":"CBERCBER","TRIP_FLOW":"YES","SKIN":"CX","EXTERNAL_ID":"0000OgssFmJOonnil9HQJVFsE6p%3A-1","COUNTRY":"CN","FROM_SITE":"CX","B_LOCATION_2":"","B_LOCATION_1":"CAN","E_LOCATION_2":"","E_LOCATION_1":"SIN","B_DATE_1":"201611100000","B_DATE_2":"","TRAVELLER_TYPE_1":"ADT","HAS_INFANT_1":"","TRAVELLER_TYPE_2":"","HAS_INFANT_2":"","TRAVELLER_TYPE_3":"","HAS_INFANT_3":"","TRAVELLER_TYPE_4":"","HAS_INFANT_4":"","TRAVELLER_TYPE_5":"","HAS_INFANT_5":"","TRAVELLER_TYPE_6":"","HAS_INFANT_6":"","TRAVELLER_TYPE_7":"","HAS_INFANT_7":"","TRAVELLER_TYPE_8":"","HAS_INFANT_8":"","TRAVELLER_TYPE_9":"","HAS_INFANT_9":"","TRIP_TYPE":"O","COMMERCIAL_FARE_FAMILY_1":"CFFECO","COMMERCIAL_FARE_FAMILY_2":"","COMMERCIAL_FARE_FAMILY_3":"","DIRECT_NON_STOP":"","PRICING_TYPE":"I","DISPLAY_TYPE":"1","WDS_METHODS_OF_PAYMENT":"CREDITCARD","WDS_METHODS_OF_DELIVERY":"ETCKT","WDS_MOD_DESC_AIRL":"","WDS_MOD_DESC_DELIV":"","WDS_MOD_DESC_ETCKT":"e-Ticket","WDS_MOD_DESC_HAND":"","WDS_MOD_DESC_PICK":"","WDS_INCLUDE_TAX":"FALSE","WDS_PROPOSE_UPSELL":"TRUE","WDS_NEXT_CABIN":"","WDS_FROM_CALENDAR":"TRUE","FIRST_PAGE":"FFCL","PROMO_CODE":"","CALENDAR_PRICE_SELECTED":"","WDS_DATE":"201611100000"}
    data = urllib.urlencode(dat2)
    request = urllib2.Request(url2,data, headers)
    response = urllib2.urlopen(request)
    page = response.read()
    #requests
    return page
"""

def get_page(url,dat):
    #url="https://book.cathaypacific.com/pl/CathayPacificV2/wds/OverrideServlet?WDS_JS_TRACE_OFF"
    s = requests.Session()
    s.headers= {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Content-Type":"application/x-www-form-urlencoded",
        "Connection":"keep-alive",
    }
    #[("a",123),("a", 345)].append(("a", "13434"))
    s.get("https://www.cathaypacific.com/cx/sc_CN.html")
    #s.header
    ret=s.post(url, data=dat)
    return ret

def get_fares():
    #url2="https://book.cathaypacific.com/pl/CathayPacificV2/wds/FlexPricerAvailabilityServlet;jsessionid=9JdMKtsfoU7lvH4jVBKcbibUz_dHA6voAVlWsE9-cSG_i9VwEP8H!2137495314!-1683833871"
    #dat2={"LANGUAGE":"CN","SITE":"CBERCBER","TRIP_FLOW":"YES","SKIN":"CX","EXTERNAL_ID":"0000OgssFmJOonnil9HQJVFsE6p%3A-1","COUNTRY":"CN","FROM_SITE":"CX","B_LOCATION_2":"","B_LOCATION_1":"CAN","E_LOCATION_2":"","E_LOCATION_1":"SIN","B_DATE_1":"201611100000","B_DATE_2":"","TRAVELLER_TYPE_1":"ADT","HAS_INFANT_1":"","TRAVELLER_TYPE_2":"","HAS_INFANT_2":"","TRAVELLER_TYPE_3":"","HAS_INFANT_3":"","TRAVELLER_TYPE_4":"","HAS_INFANT_4":"","TRAVELLER_TYPE_5":"","HAS_INFANT_5":"","TRAVELLER_TYPE_6":"","HAS_INFANT_6":"","TRAVELLER_TYPE_7":"","HAS_INFANT_7":"","TRAVELLER_TYPE_8":"","HAS_INFANT_8":"","TRAVELLER_TYPE_9":"","HAS_INFANT_9":"","TRIP_TYPE":"O","COMMERCIAL_FARE_FAMILY_1":"CFFECO","COMMERCIAL_FARE_FAMILY_2":"","COMMERCIAL_FARE_FAMILY_3":"","DIRECT_NON_STOP":"","PRICING_TYPE":"I","DISPLAY_TYPE":"1","WDS_METHODS_OF_PAYMENT":"CREDITCARD","WDS_METHODS_OF_DELIVERY":"ETCKT","WDS_MOD_DESC_AIRL":"","WDS_MOD_DESC_DELIV":"","WDS_MOD_DESC_ETCKT":"e-Ticket","WDS_MOD_DESC_HAND":"","WDS_MOD_DESC_PICK":"","WDS_INCLUDE_TAX":"FALSE","WDS_PROPOSE_UPSELL":"TRUE","WDS_NEXT_CABIN":"","WDS_FROM_CALENDAR":"TRUE","FIRST_PAGE":"FFCL","PROMO_CODE":"","CALENDAR_PRICE_SELECTED":"","WDS_DATE":"201611100000"}
    url2="https://book.cathaypacific.com/pl/CathayPacificV2/wds/FlexPricerAvailabilityServlet;jsessionid=3wlNxTkmSnSPoKuulR3EDvN5JyYiEzcTiO8kBGvm4oX9685rx_qj!614976669!492180098"
    dat2={"LANGUAGE":"CN","SITE":"CBERCBER","TRIP_FLOW":"YES","SKIN":"CX","EXTERNAL_ID":"0000I26d1yJv4iBjOPwGdAPxJCS%3A-1","COUNTRY":"CN","FROM_SITE":"CX","B_LOCATION_2":"","B_LOCATION_1":"CAN","E_LOCATION_2":"","E_LOCATION_1":"SIN","B_DATE_1":"201611100000","B_DATE_2":"","TRAVELLER_TYPE_1":"ADT","HAS_INFANT_1":"","TRAVELLER_TYPE_2":"","HAS_INFANT_2":"","TRAVELLER_TYPE_3":"","HAS_INFANT_3":"","TRAVELLER_TYPE_4":"","HAS_INFANT_4":"","TRAVELLER_TYPE_5":"","HAS_INFANT_5":"","TRAVELLER_TYPE_6":"","HAS_INFANT_6":"","TRAVELLER_TYPE_7":"","HAS_INFANT_7":"","TRAVELLER_TYPE_8":"","HAS_INFANT_8":"","TRAVELLER_TYPE_9":"","HAS_INFANT_9":"","TRIP_TYPE":"O","COMMERCIAL_FARE_FAMILY_1":"CFFECO","COMMERCIAL_FARE_FAMILY_2":"","COMMERCIAL_FARE_FAMILY_3":"","DIRECT_NON_STOP":"","PRICING_TYPE":"I","DISPLAY_TYPE":"1","WDS_METHODS_OF_PAYMENT":"CREDITCARD","WDS_METHODS_OF_DELIVERY":"ETCKT","WDS_MOD_DESC_AIRL":"","WDS_MOD_DESC_DELIV":"","WDS_MOD_DESC_ETCKT":"e-Ticket","WDS_MOD_DESC_HAND":"","WDS_MOD_DESC_PICK":"","WDS_INCLUDE_TAX":"FALSE","WDS_PROPOSE_UPSELL":"TRUE","WDS_NEXT_CABIN":"","WDS_FROM_CALENDAR":"TRUE","FIRST_PAGE":"FFCL","PROMO_CODE":"","CALENDAR_PRICE_SELECTED":"","WDS_DATE":"201611100000"}
    ret2=get_page(url2,dat2)

    if ret2.ok:
        txt=ret2.content
    else:
        txt=""

    html=etree.HTML(txt)
    #result=html.xpath('//*[@class="first"]')
    charge=html.xpath('//*[@name="WDS_GROUP"][@value="CANECOSRSALowest"]//span[2]') #票价

    jsessionid=url2[url2.find(';'):]
    url3="https://book.cathaypacific.com/pl/CathayPacificV2/wds/FareServlet"#;jsessionid=KphNJRTKz65X34rOE5YpKC3bpd58RF-p7mKA16VIdOFNWcKRP5kA!1196822677!119305406"
    url3=url3 + jsessionid

    essfield=['LANGUAGE', 'SITE', 'PRICING_TYPE', 'FIRST_PAGE', 'TRIP_TYPE', 'SKIN']
    dat3={}
    for f in essfield:
        dat3[f]=dat2[f]

    dat3.update({"flexPricerOutboundCalendarHour":"0000",
          "ASKED_FF":"CANECORSSA",
          "RECOMMENDATION_ID_1":"7",
          "PROPOSE_BUYUP":"TRUE","PAGE_TICKET":"1",
          "WDS_GROUP":"CANECORSSALowest",
          #机舱类型 经济舱special:CANECORSSALowest,经济舱core:"CANECOSRSALowest",
          # 经济舱standard:CANECOSFSALowest,经济舱flax:CANECOFFSALowest,
          # 特选经济舱:CANPEYFFSALowest
          "flexPricerOutboundCalendarDay":"10",
          "flexPricerOutboundCalendarMonthYear":"112016",
          "FLIGHT_ID_1":"0"})

    ret3=get_page(url3,dat3)
    return ret3

def select_datetime():
    name="FLIGHT_ID_1"
    value="1"
    return name

def person_info():
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
    t=get_fares()








