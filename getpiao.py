#!-*- coding:utf-8 -*-
__author__ = 'Administrator'
import requests
#import urllib2
#import urllib
import re
import datetime
from lxml import etree
from bs4 import BeautifulSoup
#from selenium import webdriver
# 查询机票 --->选择机票---->生成订单----->付款
#
#
#
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

#请求下载页面
def request_page(url,dat):
    s = requests.Session()
    s.headers= {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Content-Type":"application/x-www-form-urlencoded",
        "Connection":"keep-alive"
    }
    s.get("https://www.cathaypacific.com/cx/sc_CN.html")
    ret=s.post(url,data=dat)
    return ret

#解析票价页面
def parse_fare(htmlstr):
    #soup = BeautifulSoup(open('testparse.html'))
    #print soup.prettify()
    soup=BeautifulSoup(htmlstr)
    ret=soup.find_all("tr",re.compile("flightEffectOff*"))
    all_flight=[]
    a_flight=[]
    for i in ret:
        flight={}
        if i.find("input",class_="radio"):
            if a_flight:
                all_flight.append(a_flight)
                a_flight=[]
            flight['ban']=i.find('span',class_="icono").text  #航班号
            trip=i.select('td[class="first"]')
            flight['ftrip']=trip[0].text
            flight['btrip']=trip[1].text
            flight['station']=i.select('td[class="centeralign first textAlignRight"]').text
            flight['ntime']=i.select('td[class="duration textAlignRight "]')
            flight['crafttype']=i.find('a',class_="aircraft").text
            a_flight.append(flight)
        elif i.find("span",class_="optext"):
            flight['yunying']=i.select('span[class="optext"]')[0].text
            a_flight.append(flight)
        else:
            flight['ban']=i.find('span',class_="icono").text  #航班号
            trip=i.select('td[class="first"]')
            flight['ftrip']=trip[0].text
            flight['btrip']=trip[1].text
            flight['station']=i.select('td[class="centeralign first textAlignRight"]').text
            flight['crafttype']=i.find('a',class_="aircraft").text
            a_flight.append(flight)
    all_flight.append(a_flight)
    charge={}
    chargetable=soup.find("table",id="fareFamilyReloadedTable")

    charge['special']=chargetable.find("input",value="CANECORSSALowest").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
    charge['core']=chargetable.find("input",value="CANECORSSALowest").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
    charge['standard']=chargetable.find("input",value="CANECORSSALowest").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
    charge['flex']=chargetable.find("input",value="CANECORSSALowest").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
    charge['special_flex']=chargetable.find("input",value="CANECORSSALowest").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
    all_flight.append(charge)
    return all_flight

#获取今后的第n天
def getndate(n):
    return (datetime.date.today() + datetime.timedelta(days=n)).strftime("%Y%m%d")

#获取时间戳
def GetTimeStamp():
    return datetime.datetime.now().strftime("%d%m%Y%H%M")

def get_fares():
    #初始化请求request
    s = requests.Session()
    s.headers= {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Accept-Encoding":"gzip, deflate, br",
        #"Accept-Language":"zh-CN,zh;q=0.8",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Content-Type":"application/x-www-form-urlencoded",
        "Connection":"keep-alive"
    }
    s.get("https://www.cathaypacific.com/cx/sc_CN.html")
    url1="https://book.cathaypacific.com/pl/CathayPacificV2/wds/OverrideServlet?WDS_JS_TRACE_OFF"
    tomorrow=getndate(1)
    theyear=tomorrow[0:4]
    themonth=tomorrow[4:6]
    theday=tomorrow[4:6]
    #固定参数
    dat1={"SITE":"CBERCBER","DATE_RANGE_QUALIFIER_2":"C","DATE_RANGE_VALUE_1":"3","WDS_METHODS_OF_PAYMENT":"CREDITCARD","SO_SITE_PENDING_TIME_LIMIT":"H25","SO_SITE_SPEC_SERV_CHARGEABLE":"TRUE","WDS_BOH_FEE":"0","SO_SITE_FP_NB_RECO":"200","CSE_ENABLE":"TRUE","SO_SITE_ETKT_Q_AND_CAT":"10C98","WDS_LSA_FIR":"2","WDS_LSA_ECO":"8","PRICING_TYPE":"I","DISPLAY_TYPE":"1","WDS_INCLUDE_TAX":"FALSE","SO_SITE_QUEUE_OFFICE_ID":"BJSCX08AA","WDS_NME_ACTIVATED":"TRUE","WDS_LSA_PEY":"6", "DATE_RANGE_QUALIFIER_1":"C","SO_SITE_OFFICE_ID":"BJSCX08AA","WDS_AM_ENROLLMENT_ACTIVATED":"TRUE","DATE_RANGE_VALUE_2":"3","COMMERCIAL_FARE_FAMILY_1":"CFFECO","WDS_MOD_DESC_ETCKT":"e-Ticket","SO_SITE_NB_FLIGHTS_AVAIL":"50","SO_SITE_ETKT_Q_OFFICE_ID":"HKGCX08AA","SO_SITE_ALLOW_LSA_INDICATOR":"TRUE",}
    #dat1={"WDS_METHODS_OF_PAYMENT":"CREDITCARD","SO_SITE_PENDING_TIME_LIMIT":"H25","TRIP_FLOW":"YES","EMBEDDED_TRANSACTION":"FlexPricerAvailabilityServlet","WDS_RED_DOMAIN":"www.cathaypacific.com","TRAVELLER_TYPE_1":"ADT","WDS_BOH_BLOCKED":"72","EXTERNAL_ID":"0000OXvn4U5KMBEzz0VyEPYQnBO%3A-1","TRIP_TYPE":"O","WDS_METHODS_OF_DELIVERY":"ETCKT","WDS_IS_TRP_ENABLED":"FALSE","SO_SITE_IS_INSURANCE_ENABLED":"FALSE","WDS_AM_ENROLLMENT_BONUS":"0","RETURNURL":"http%3A%2F%2Fwww.cathaypacific.com%3A80%2Fcx%2Fsc_CN%2F_jcr_content.handler.html","SO_SITE_QUEUE_CATEGORY":"27C1","WDS_LSA_BUS":"6","SO_GL":"%3C%3Fxml+version%3D%221.0%22+encoding%3D%22UTF-8%22%3F%3E%3CSO_GL%3E%3CGLOBAL_LIST%3E%3CNAME%3ESITE_SITE_FARE_COMMANDS_AND_OPTIONS%3C%2FNAME%3E%3CLIST_ELEMENT%3E%3CCODE%3E105%3C%2FCODE%3E%3CLIST_VALUE+null%3D%22false%22%3E0%3C%2FLIST_VALUE%3E%3CLIST_VALUE+null%3D%22false%22%3E2%3C%2FLIST_VALUE%3E%3CLIST_VALUE+null%3D%22false%22%3E4%3C%2FLIST_VALUE%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22false%22%3E0%3C%2FLIST_VALUE%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3C%2FLIST_ELEMENT%3E%3C%2FGLOBAL_LIST%3E%3CGLOBAL_LIST%3E%3CNAME%3ESITE_SITE_FARE_BACKUP_COMMANDS_AND_OPTIONS%3C%2FNAME%3E%3CLIST_ELEMENT%3E%3CCODE%3E105%3C%2FCODE%3E%3CLIST_VALUE+null%3D%22false%22%3E0%3C%2FLIST_VALUE%3E%3CLIST_VALUE+null%3D%22false%22%3E2%3C%2FLIST_VALUE%3E%3CLIST_VALUE+null%3D%22false%22%3E4%3C%2FLIST_VALUE%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22false%22%3E0%3C%2FLIST_VALUE%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3C%2FLIST_ELEMENT%3E%3C%2FGLOBAL_LIST%3E%3CGLOBAL_LIST%3E%3CNAME%3ESITE_SERVICE_FEE%3C%2FNAME%3E%3CLIST_ELEMENT%3E%3CCODE%3E0%3C%2FCODE%3E%3CLIST_VALUE+null%3D%22false%22%3E1%3C%2FLIST_VALUE%3E%3CLIST_VALUE+null%3D%22false%22%3E1%3C%2FLIST_VALUE%3E%3CLIST_VALUE+null%3D%22false%22%3E0%3C%2FLIST_VALUE%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22false%22%3E3%3C%2FLIST_VALUE%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3CLIST_VALUE+null%3D%22true%22%2F%3E%3C%2FLIST_ELEMENT%3E%3C%2FGLOBAL_LIST%3E%3C%2FSO_GL%3E","SO_SITE_SPEC_SERV_CHARGEABLE":"TRUE","WDS_BOH_FEE":"0","SO_SITE_FP_NB_RECO":"200","CSE_ENABLE":"TRUE","SO_SITE_ETKT_Q_AND_CAT":"10C98","TIME_STAMP":"111120161910","WDS_LSA_FIR":"2","WDS_LSA_ECO":"8","PRICING_TYPE":"I","WDS_URL_CATHAY":"https%3A%2F%2Fwww.cathaypacific.com%2Fwdsibe%2FIBEFacade","WDS_BOH_ACTIVATED":"TRUE","WDS_AM_ENROLLMENT_PROMO_MESSAGE":"%E5%B0%9A%E6%9C%AA%E6%88%90%E4%B8%BA%E3%80%8C%E4%BA%9A%E6%B4%B2%E4%B8%87%E9%87%8C%E9%80%9A%E3%80%8D%E4%BC%9A%E5%91%98%EF%BC%9F","DISPLAY_TYPE":"1","WDS_INCLUDE_TAX":"FALSE","SO_SITE_QUEUE_OFFICE_ID":"BJSCX08AA","FROM_SITE":"CX","MARKET":"CN","WDS_NME_ACTIVATED":"TRUE","B_LOCATION_1":"CAN","WDS_LSA_PEY":"6","SITE":"CBERCBER","DATE_RANGE_QUALIFIER_1":"C","SO_SITE_OFFICE_ID":"BJSCX08AA","DATE_RANGE_QUALIFIER_2":"C","DATE_RANGE_VALUE_1":"3","WDS_AM_ENROLLMENT_ACTIVATED":"TRUE","DATE_RANGE_VALUE_2":"3","COMMERCIAL_FARE_FAMILY_1":"CFFECO","SO_SITE_OH_USE_BKDATE_BUF":"TRUE","errorFlow":"error","WDS_BOH_TYPE":"NO_DEPOSIT","LANGUAGE":"CN","WDS_NEXTCABIN":"NONE","E_LOCATION_1":"SIN","WDS_MOD_DESC_ETCKT":"e-Ticket","WDS_FFP_LIST":"CX%3AEI%3ACA%3ANZ%3AAB%3AAS%3AAA%3APG%3ABA%3AAY%3AIB%3AJL%3A9W%3ALA%3AMH%3AQF%3AQR%3ARJ%3AS7%3AUL%3AJJ","ERRORURL":"http%3A%2F%2Fwww.cathaypacific.com%3A80%2Fcx%2Fsc_CN%2F_jcr_content.handler.html%3FFORMID%3Dundefined","WDS_PROPOSE_UPSELL":"TRUE","BOOKING_FLOW":"REVENUE","COUNTRY":"CN","WDS_OWPARTNER_LIST":"AB%3AAA%3ABA%3AAY%3AIB%3AJL%3ALA%3AMH%3AQF%3AQR%3ARJ%3AS7%3AUS%3AUL%3AJJ","CHECKSUM_ENTRY_FLOW":"C59FF5DE26A03DDDCA80ED8BD59B9798","SO_SITE_CHARGEABLE_SEATMAP":"TRUE","SO_SITE_RM_FARE_TYPE":"TRUE","B_DATE_1":"201611120000","SKIN":"CX","SO_SITE_NB_FLIGHTS_AVAIL":"50","SO_SITE_ETKT_Q_OFFICE_ID":"HKGCX08AA","SO_SITE_ALLOW_LSA_INDICATOR":"TRUE","ENTRYCOUNTRY":"CN","ENTRYLANGUAGE":"sc"}
    #可配置的参数
    dat1.update({
        "TIME_STAMP":GetTimeStamp(),#"111120161539",
        "B_DATE_1":tomorrow+"0000",#"201611110000",
        "LANGUAGE":"CN",
        "SKIN":"CX",
        "B_LOCATION_1":"CAN",
        "E_LOCATION_1":"SIN",
        "COUNTRY":"CN",
        "FROM_SITE":"CX",
        "MARKET":"CN",
        "ENTRYCOUNTRY":"CN",
        "ENTRYLANGUAGE":"sc",
    })
    ret1=s.post(url1,data=dat1)
    jsession_pattern=re.compile('jsessionid.{0,120}[0-9]')
    content1 = ret1.content
    print u"获取到第一个页面"
    t=jsession_pattern.findall(content1)

    if t:
        jsessionid=t[0]
        print u"获取到jSESSION_ID:%s"%(jsessionid)
    else:
        print u"未取到数据，可能频率限制"
        return
    #jsessionid=""
    url2="https://book.cathaypacific.com/pl/CathayPacificV2/wds/FlexPricerAvailabilityServlet;"
    url2=url2+jsessionid
#dat2={"LANGUAGE":"CN","SITE":"CBERCBER","TRIP_FLOW":"YES","SKIN":"CX","EXTERNAL_ID":"0000I26d1yJv4iBjOPwGdAPxJCS%3A-1","COUNTRY":"CN","FROM_SITE":"CX","B_LOCATION_2":"","B_LOCATION_1":"CAN","E_LOCATION_2":"","E_LOCATION_1":"SIN","B_DATE_1":"201611100000","B_DATE_2":"","TRAVELLER_TYPE_1":"ADT","HAS_INFANT_1":"","TRAVELLER_TYPE_2":"","HAS_INFANT_2":"","TRAVELLER_TYPE_3":"","HAS_INFANT_3":"","TRAVELLER_TYPE_4":"","HAS_INFANT_4":"","TRAVELLER_TYPE_5":"","HAS_INFANT_5":"","TRAVELLER_TYPE_6":"","HAS_INFANT_6":"","TRAVELLER_TYPE_7":"","HAS_INFANT_7":"","TRAVELLER_TYPE_8":"","HAS_INFANT_8":"","TRAVELLER_TYPE_9":"","HAS_INFANT_9":"","TRIP_TYPE":"O","COMMERCIAL_FARE_FAMILY_1":"CFFECO","COMMERCIAL_FARE_FAMILY_2":"","COMMERCIAL_FARE_FAMILY_3":"","DIRECT_NON_STOP":"","PRICING_TYPE":"I","DISPLAY_TYPE":"1","WDS_METHODS_OF_PAYMENT":"CREDITCARD","WDS_METHODS_OF_DELIVERY":"ETCKT","WDS_MOD_DESC_AIRL":"","WDS_MOD_DESC_DELIV":"","WDS_MOD_DESC_ETCKT":"e-Ticket","WDS_MOD_DESC_HAND":"","WDS_MOD_DESC_PICK":"","WDS_INCLUDE_TAX":"FALSE","WDS_PROPOSE_UPSELL":"TRUE","WDS_NEXT_CABIN":"","WDS_FROM_CALENDAR":"TRUE","FIRST_PAGE":"FFCL","PROMO_CODE":"","CALENDAR_PRICE_SELECTED":"","WDS_DATE":"201611100000"}
#"DIRECT_NON_STOP":"","FIRST_PAGE":"FFCL","WDS_NEXT_CABIN":"","PROMO_CODE":"","CALENDAR_PRICE_SELECTED":"","DISPLAY_TYPE":"1", "WDS_MOD_DESC_AIRL":"","WDS_MOD_DESC_DELIV":"","WDS_MOD_DESC_ETCKT":"e-Ticket","WDS_MOD_DESC_HAND":"","WDS_MOD_DESC_PICK":"",
    dat2={"LANGUAGE":"CN","SITE":"CBERCBER","TRIP_FLOW":"YES","SKIN":"CX",
          "COUNTRY":"CN","FROM_SITE":"CX","PRICING_TYPE":"I",
          "B_LOCATION_2":"","B_LOCATION_1":"CAN","E_LOCATION_2":"","E_LOCATION_1":"SIN",
          "B_DATE_1":"201611100000","B_DATE_2":"","TRAVELLER_TYPE_1":"ADT","HAS_INFANT_1":"",
          "TRIP_TYPE":"O","COMMERCIAL_FARE_FAMILY_1":"CFFECO",
          "WDS_METHODS_OF_PAYMENT":"CREDITCARD","WDS_METHODS_OF_DELIVERY":"ETCKT",
          "WDS_INCLUDE_TAX":"FALSE","EXTERNAL_ID":"0000I26d1yJv4iBjOPwGdAPxJCS%3A-1",
          "WDS_PROPOSE_UPSELL":"TRUE","WDS_FROM_CALENDAR":"TRUE",
          "WDS_DATE":"201611100000"}
    #选择日期
    dat2.update({
        "B_DATE_1":dat1["B_DATE_1"],#"201611100000",
        "WDS_DATE":dat1["B_DATE_1"],#"201611100000"
    })
    ret2=s.post(url2,data=dat2)
    if ret2.ok:
        txt=ret2.content
    else:
        txt=""
    html=etree.HTML(txt)
    print u"获取到第二个页面"
    #result=html.xpath('//*[@class="first"]')
    result=html.xpath('/html/body//div[@id="FFCO"]//tbody[@id="mainTabContent"]/tr//*')
    #看票价
    charge=html.xpath('//*[@name="WDS_GROUP"][@value="CANECOSRSALowest"]//span[2]') #票价

    dat3f={"BACKUP_TO_FULL_RULES":"true","RULE_SOURCE_1_TYPE":"FARE","RULE_SOURCE_1_ID":"","FROM_FLOW_TRANSACTION":"","FROM_FLOW_INITIAL_PRODUCT":"","FROM_FLOW_BOOKING_TYPE":"","FROM_FLOW_FEATURE_1_CODE":"",}
    dat3f.update({
        "LANGUAGE":"CN",
        "TRANSACTION_ID":"MiniRules",
        "JSESSION_ID":jsessionid[11:],
        "SITE":"CBERCBER",})
    url3f="https://book.cathaypacific.com/pl/CathayPacificV2/wds/MiniRulesServlet;"+jsessionid
    ret3f=s.post(url3f,data=dat3f)
    #选择机票
    url3="https://book.cathaypacific.com/pl/CathayPacificV2/wds/FareServlet;"#jsessionid=KphNJRTKz65X34rOE5YpKC3bpd58RF-p7mKA16VIdOFNWcKRP5kA!1196822677!119305406"
    url3=url3 + jsessionid
    essfield=['LANGUAGE', 'SITE', 'PRICING_TYPE', 'SKIN'] # 'FIRST_PAGE','TRIP_TYPE',
    dat3={}
    for f in essfield:
        dat3[f]=dat2[f]
    dat3.update({
        "flexPricerOutboundCalendarHour":"0000",
        "ASKED_FF":"CANECORSSA",
        "RECOMMENDATION_ID_1":"7",
        "PROPOSE_BUYUP":"TRUE",
        #"PAGE_TICKET":"1",
    })
    dat3.update({
          "WDS_GROUP":"CANECORSSALowest",
          #机舱类型 经济舱special:CANECORSSALowest,经济舱core:"CANECOSRSALowest",
          # 经济舱standard:CANECOSFSALowest,经济舱flax:CANECOFFSALowest,
          # 特选经济舱:CANPEYFFSALowest
          "flexPricerOutboundCalendarDay":theday,#"10",
          "flexPricerOutboundCalendarMonthYear":themonth+theyear,#"112016",
          "FLIGHT_ID_1":"0"
    })
    ret3=s.post(url3,data=dat3)

    url4="https://book.cathaypacific.com/pl/CathayPacificV2/wds/OverrideServlet;"
    dat4={"EMBEDDED_TRANSACTION":"AddElementsServlet",
          "LANGUAGE":"CN","SITE":"CBERCBER","CABIN":"M","PAGE_TICKET":"2",
          "TYPE":"AIR_TRIP_FARE",
          "WDS_MILES_EARNED_STR":"161120162215%2C161120162320%2C171120160900%2C171120161300CX%2CCXKA%2CCX5789%2C759L%2CLCAN%2CHKG%2CHKG%2CSIN16760150",
          "WDS_CLUBPOINTS_EARNED_STR":"",
          "WDS_OFFSET_CARBON_STR":"",
          "WDS_SEAT_STR":"161120162215%2C161120162320%2C171120160900%2C171120161300CX%2CCX5789%2C759L%2CLCAN%2CHKG%2CHKG%2CSINtruetrue",
          "WDS_OFFSET_CARBON_CHECKSUM":"",
          #需要验证的字符串
          "WDS_MILES_EARNED_CHECKSUM":"9685C391758DED8A3BDAE7360F47CBD8",
          "WDS_SEAT_CHECKSUM":"9E8270038C16E3066EAE32F66941A65B",
          "WDS_MILES_RESPONSE":"earnedMiles%3D1676%3AbonusMiles%3D0%3AbonusMilesLink%3D%3AaAdvantageEligible%3Dfalse%3AtotalMiles%3D1676%3AearnedPoints%3D15%3AbonusPoints%3D0%3AbonusPointsLink%3D%3APointsaAdvantageEligible%3Dfalse%3AtotalPoints%3D15",
          "WDS_CLUBPOINTS_RESPONSE":"",
          "WDS_CARBON_RESPONSE":"",
          "WDS_SEATS_RESPONSE":"SEAT_0_0%3Dtrue%3ASEAT_0_1%3Dtrue",
          "FIRST_PAGE":"FFCL",
          "MINI_RULES_AJAX_SUCCESS":"true",
          "SERVICE_POLICY_AJAX_SUCCESS":"true",
          "CONVERT_CURRENCY":"NO","WDS_CARBON_RADIO":"FALSE",
          "LATE_LOGIN":"FALSE","LOGIN":"","PASSWORD":""}
    ret4=s.post(url4,data=dat4)
    #生成订单添加元素
    url5="https://book.cathaypacific.com/pl/CathayPacificV2/wds/AddElementsServlet;"
    url5=url5+jsessionid
    dat5={"SITE","CBERCBER","LANGUAGE","CN","PAGE_TICKET","3","FROM_PAX","TRUE","DELIVERY_TYPE","ETCKT","NB_ADT","1","NB_CHD","0","NB_INF","0","Dyc_EMAI","%3Cdiv+class%3D%22dync_content%22%3E+++++++++%3Ch2+style%3D%22color%3A%23006564%3Bmargin%3A+10px+0+10px+0%3B+font-family%3AAktiv+Grotesk+W01+Regular%2CArial%2CHelvetica%2CSans-serif%3B+font-size%3A+1.45em%3B+font-weight%3A+300%3B+text-align%3A+left%3B%22%3E%E6%97%85%E6%B8%B8%E6%8F%90%E7%A4%BA%3C%2Fh2%3E+++%3Cdiv+style%3D%22width%3A190px%3Bfloat%3Aleft%3Bmargin%3A5px%22%3E%3Ca+class%3D%22right-arrow-icon%22+style%3D%22color%3A%230f7e92%3Bline-height%3A23px%3Btext-decoration%3Anone%3B%22+target%3D%22_blank%22+href%3D%22https%3A%2F%2Fwww.cathaypacific.com%2Fcx%2Fsc_CN%2Fmanage-booking.html%3Futm_channel%3DEDM%26amp%3Butm_source%3DCX_SERVICES%26amp%3Butm_medium%3DIBE_REV_CONF%26amp%3Butm_campaign%3DMMB%26amp%3Butm_content%3DMMB%26amp%3Butm_term%3DFOOTER%22%3E%E7%AE%A1%E7%90%86%E8%A1%8C%E7%A8%8B%3C%2Fa%3E%3C%2Fdiv%3E%3Cdiv+style%3D%22width%3A190px%3Bfloat%3Aleft%3Bmargin%3A5px%22%3E%3Ca+class%3D%22right-arrow-icon%22+style%3D%22color%3A%230f7e92%3Bline-height%3A23px%3Btext-decoration%3Anone%3B%22+target%3D%22_blank%22+href%3D%22https%3A%2F%2Fwww.cathaypacific.com%2Fcx%2Fsc_CN%2Fabout-us%2Fcontact-us%2Ffaqs%2Fonline-booking-ticket-purchase%2Fchanges-cancellation-and-refund.html%3Futm_channel%3DEDM%26amp%3Butm_source%3DCX_SERVICES%26amp%3Butm_medium%3DIBE_REV_CONF%26amp%3Butm_campaign%3DCHANGE-BOOKING%26amp%3Butm_content%3DFAQ%26amp%3Butm_term%3DFOOTER%22%3E%E6%9B%B4%E6%94%B9%E8%AE%A2%E7%A5%A8%3C%2Fa%3E%3C%2Fdiv%3E%3Cdiv+style%3D%22width%3A190px%3Bfloat%3Aleft%3Bmargin%3A5px%22%3E%3Ca+class%3D%22right-arrow-icon%22+style%3D%22color%3A%230f7e92%3Bline-height%3A23px%3Btext-decoration%3Anone%3B%22+target%3D%22_blank%22+href%3D%22https%3A%2F%2Fwww.cathaypacific.com%2Fcx%2Fsc_CN%2Ftravel-information%2Ftravel-preparation%2Fvisa-information%2Fpassport-visa-information.html%3Futm_channel%3DEDM%26amp%3Butm_source%3DCX_SERVICES%26amp%3Butm_medium%3DIBE_REV_CONF%26amp%3Butm_campaign%3DVISA-INFORMATION%26amp%3Butm_content%3DTRAVEL-INFORMATION%26amp%3Butm_term%3DFOOTER%22%3E%E6%8A%A4%E7%85%A7%E7%AD%BE%E8%AF%81%E8%B5%84%E8%AE%AF%3C%2Fa%3E%3C%2Fdiv%3E%3Cdiv+style%3D%22width%3A190px%3Bfloat%3Aleft%3Bmargin%3A5px%22%3E%3Ca+class%3D%22right-arrow-icon%22+style%3D%22color%3A%230f7e92%3Bline-height%3A23px%3Btext-decoration%3Anone%3B%22+target%3D%22_blank%22+href%3D%22https%3A%2F%2Fwww.cathaypacific.com%2Fcx%2Fsc_CN%2Fmanage-booking%2Fcheck-in.html%3Futm_channel%3DEDM%26amp%3Butm_source%3DCX_SERVICES%26amp%3Butm_medium%3DIBE_REV_CONF%26amp%3Butm_campaign%3DOLCI%26amp%3Butm_content%3DOLCI%26amp%3Butm_term%3DFOOTER%22%3E%E7%BD%91%E4%B8%8A%E9%A2%84%E5%8A%9E%E7%99%BB%E6%9C%BA%3C%2Fa%3E%3C%2Fdiv%3E%3Cdiv+style%3D%22width%3A190px%3Bfloat%3Aleft%3Bmargin%3A5px%22%3E%3Ca+class%3D%22right-arrow-icon%22+style%3D%22color%3A%230f7e92%3Bline-height%3A23px%3Btext-decoration%3Anone%3B%22+target%3D%22_blank%22+href%3D%22https%3A%2F%2Fitunes.apple.com%2Fau%2Fapp%2Fcx-discovery%2Fid545892116%3Fmt%3D8%22%3EDiscovery+%E8%88%AA%E7%A9%BA%E6%9D%82%E5%BF%97%3C%2Fa%3E%3C%2Fdiv%3E%3Cdiv+style%3D%22width%3A190px%3Bfloat%3Aleft%3Bmargin%3A5px%22%3E%3Ca+class%3D%22right-arrow-icon%22+style%3D%22color%3A%230f7e92%3Bline-height%3A23px%3Btext-decoration%3Anone%3B%22+target%3D%22_blank%22+href%3D%22https%3A%2F%2Fwww.cathaypacific.com%2Fcx%2Fsc_CN%2Ftravel-information%2Fairport.html%3Futm_channel%3DEDM%26amp%3Butm_source%3DCX_SERVICES%26amp%3Butm_medium%3DIBE_REV_CONF%26amp%3Butm_campaign%3DAIRPORT-INFOMRATION%26amp%3Butm_content%3DTRAVEL-INFORMARTION%26amp%3Butm_term%3DFOOTER+%22%3E%E6%9C%BA%E5%9C%BA%E8%B5%84%E6%96%99%3C%2Fa%3E%3C%2Fdiv%3E+++%3Cbr+style%3D%22clear%3Aboth%22%3E+++%3Cp+style%3D%22color%3A%234c4c4c%3Bfont-family%3AAktiv+Grotesk+W01+Regular%2CArial%2CHelvetica%2CSans-serif%3B%22%3E%E6%88%96%E8%81%94%E7%B3%BB+%3Ca+target%3D%22_blank%22+style%3D%22color%3A%230f7e92%3Btext-decoration%3Anone%3B%22+href%3D%22https%3A%2F%2Fwww.cathaypacific.com%2Fcx%2Fsc_CN%2Fabout-us%2Fcontact-us%2Fglobal-contact-centres.html%3Futm_channel%3DEDM%26amp%3Butm_source%3DCX_SERVICES%26amp%3Butm_medium%3DIBE_REV_CONF%26amp%3Butm_campaign%3DCONTACT-GCC%26amp%3Butm_content%3DCONTACT-US%26amp%3Butm_term%3DFOOTER%22%3E%E5%85%A8%E7%90%83%E5%AE%A2%E6%88%B7%E6%9C%8D%E5%8A%A1%E4%B8%AD%E5%BF%83%3C%2Fa%3E%3C%2Fp%3E+++%3C%2Fdiv%3E","Dyc_EMAI_2","","Dyc_EMAI_BOH","","DycTerms_EMAI","","WDS_ALPI","TRUE","POPIN_CANCEL","","CONTACT_POINT_HOME_PHONE_OC","","CONTACT_POINT_HOME_PHONE_AC","","CONTACT_POINT_BUSINESS_PHONE_OC","","CONTACT_POINT_BUSINESS_PHONE_AC","","CONTACT_POINT_MOBILE_1_OC","","CONTACT_POINT_MOBILE_1_AC","","NOTIF_TYPE_1_1","E","NOTIF_VALUE_1_1","2231686756%40qq.com","NOTIF_TYPE_1_2","M","NOTIF_VALUE_1_2","15671532758","NOTIF_OVERSEAS_CODE_1_2","86","WDS_CREDITCARD_LIST","","WDS_DEBITCARD_LIST","CU","PSP_LIST","adyen%2Cbtb","WDS_VI","","WDS_CA","","WDS_AX","","WDS_TP","","WDS_DC","","WDS_JC","","Dyc_PURC_msg","","Dyc_PURC_display","","WDS_FXMPCARD_LIST","VI%3ACA","IDENTITY_DOCUMENT_GENDER_PSPT_0","","IDENTITY_DOCUMENT_NATIONALITY_PSPT_0","","IDENTITY_DOCUMENT_DATE_OF_BIRTH_PSPT_0","","IDENTITY_DOCUMENT_LAST_NAME_PSPT_0","","IDENTITY_DOCUMENT_FIRST_NAME_PSPT_0","","IDENTITY_DOCUMENT_MIDDLE_NAME_PSPT_0","","IDENTITY_DOCUMENT_TYPE_PSPT_0","","IDENTITY_DOCUMENT_NUMBER_PSPT_0","","IDENTITY_DOCUMENT_ISSUING_COUNTRY_PSPT_0","","IDENTITY_DOCUMENT_EXPIRY_DATE_PSPT_0","","IDENTITY_DOCUMENT_TYPE_VISA_0","","IDENTITY_DOCUMENT_NUMBER_VISA_0","","IDENTITY_PLACE_OF_ISSUING_VISA_0","","IDENTITY_DOCUMENT_ISSUE_DATE_VISA_0","","IDENTITY_DOCUMENT_APPLICABLE_COUNTRY_VISA_0","","IDENTITY_DOCUMENT_PLACE_OF_BIRTH_VISA_0","","APIS_ADDRESS_FIRSTLINE_R_0","","APIS_ADDRESS_SECONDLINE_R_0","","APIS_ADDRESS_CITY_R_0","","APIS_ADDRESS_ZIPCODE_R_0","","APIS_ADDRESS_STATE_R_0","","APIS_ADDRESS_COUNTRY_R_0","","APIS_ADDRESS_FIRSTLINE_D_0","","APIS_ADDRESS_SECONDLINE_D_0","","APIS_ADDRESS_CITY_D_0","","APIS_ADDRESS_ZIPCODE_D_0","","APIS_ADDRESS_STATE_D_0","","APIS_ADDRESS_COUNTRY_D_0","","DATE_OF_BIRTH_DAY_0","","DATE_OF_BIRTH_MONTH_0","","DATE_OF_BIRTH_YEAR_0","","DATE_OF_EXPIRATION_DAY_0","","DATE_OF_EXPIRATION_MONTH_0","","DATE_OF_EXPIRATION_YEAR_0","","DATE_OF_ISSUE_DAY_0","","DATE_OF_ISSUE_MONTH_0","","DATE_OF_ISSUE_YEAR_0","","SELECT_TITLE_1","MR","TITLE_1","MR","LAST_NAME_1","wan","FIRST_NAME_1","ci","FIRST_FF_AIRLINE","","PREF_AIR_FREQ_AIRLINE_1_1","","PREF_AIR_FREQ_NUMBER_1_1","","CONTACT_POINT_EMAIL_1","2231686756%40qq.com","CONTACT_POINT_HOME_PHONE","86-15671532758","CONTACT_POINT_MOBILE","86-15671532758","CONTACT_POINT_BUSINESS_PHONE","","PHONE_TYPE","MOB","PHONE_COUNTRY","86","PHONE_AREA","","PHONE_NUMBER","15671532758","ALPI_PREF_AIR_MEAL_1","STRD","AM_adtDateOfBirthDay1","","AM_adtDateOfBirthMonth1","","AM_adtDateOfBirthYear1","","IDENTITY_DOCUMENT_NATIONALITY_PSPT_AM","","enrolment_total","","enrolment_success","","AM_notSuccessful_TravellerIDs","","AM_call_failure","","AM_TravellerID_to_FFN_Mapping","","AM_ENROLMENT_SELECTED","","REGISTRATION_STATUS","","REGISTRATION_RESPONSE_CODE","","PREF_AIR_SEAT_ASSIGMENT_1_1","","PREF_AIR_SEAT_ASSIGMENT_1_2",""}
    ret5=s.post(url5,data=dat5)
    return ret3

"""
#加密函数
WDSCommon.getTagValue=function(a,b){
    var c;
    a.tagName&&a.tagName.toUpperCase()=="FORM"&&(a=a[b]);
    if(!a){
    	return WDSTrace.dump("WDSCommon.getTagValue : input "+b+" does not exist"),"";
    }
    if(a.tagName=="SELECT"){
    	return WDSTrace.dump("WDSCommon.getTagValue : SELECT : "+a.value),a.value;
    }else{
    	if(a.tagName=="INPUT"){
    		if(a.length){
    			if(a[0].type.toUpperCase()=="RADIO"){
    				for(i=0;i<a.length;i++){
    					if(c=a[i],c.type.toUpperCase()=="RADIO"&&c.checked){
    						return WDSTrace.dump("WDSCommon.getTagValue : RADIO : "+c.value),c.value;
    					}
    				}
    			}
    		}else{
    			if(a.type.toUpperCase()=="CHECKBOX"||a.type.toUpperCase()=="RADIO"){
    				if(a.checked==!0){
    					return WDSTrace.dump("WDSCommon.getTagValue : " +a.type.toUpperCase()+" : "+a.value),a.value;
    				}
    			}else{
    				return WDSTrace.dump("WDSCommon.getTagValue : ? : "+a.value),a.value;
    			}
    		}
    	}else{
    		if(a.tagName=="TEXTAREA"){
    			return a.value;
    		}else{
    			if(a.length){
    				for(i=0;i<a.length;i++){
    					if(c=a[i],c.type.toUpperCase()=="RADIO"&&c.checked){
    						return WDSTrace.dump("WDSCommon.getTagValue : RADIO : "+a.value),c.value;
    					}
    				}
    			}else{
    				if(a.checked){
    					return WDSTrace.dump("WDSCommon.getTagValue : ? : "+a.value),a.value;
    				}
    			}
    		}
    	}
    }
    WDSTrace.dump("WDSCommon.getTagValue : bad");
    return"";
};
"""


def person_info():
    """info={"SELECT_TITLE_1":"MR",#MR,MRS,MS,MISS,DR,PROF
          "LAST_NAME_1":"wan",
          "FIRST_NAME_1":"wanchi",
          "CONTACT_POINT_EMAIL_1":"15671532758@163.com",
          "PHONE_COUNTRY":"86",
          "PHONE_AREA":"",
          "PHONE_NUMBER":"18565441226"
          }"""
    #url="https://book.cathaypacific.com/pl/CathayPacificV2/wds/OverrideServlet;jsessionid=1ytmpZfsTmLvRUZs0TTkzHE8XqHrIUcqaIBScjVWZQbE3d-i9DJ3!1912273412!-1487912580"
    #cooks={"utm":"DIRECT","optimizelyEndUserId":"oeu1479120598183r0.3173203392667969","D_SID":"183.6.134.18:W9hfggkr6h9pxNTxjUeT0hp9BIwZMGsJidmkumW1LWg","_gat_tealium_0":"1","optimizelyBuckets":"%7B%227641121066%22%3A%227645400480%22%2C%225240120018%22%3A%225230420832%22%7D","optimizelySegments":"%7B%221359740366%22%3A%22referral%22%2C%221360563911%22%3A%22gc%22%2C%221364814164%22%3A%22false%22%2C%221397001650%22%3A%22none%22%2C%221819390214%22%3A%22CN%22%2C%222008751137%22%3A%22zh_cn%22%2C%222009200416%22%3A%22zh_cn_CN%22%2C%223065330344%22%3A%22Y%22%2C%223229810736%22%3A%22Revenue_FlexPricer%22%2C%225310040163%22%3A%22true%22%2C%226311112236%22%3A%22CAN_SIN%22%7D","route":"CAN_SIN","cxRs":"{%22c%22:%22Y%22%2C%22t%22:%22O%22%2C%22o_d%22:%222016-11-16%22%2C%22o_apt%22:%22CAN%22%2C%22i_d%22:%222016-11-17%22%2C%22d_apt%22:%22SIN%22%2C%22pa%22:1%2C%22py%22:%220%22%2C%22pc%22:0%2C%22pi%22:0}","_ga":"GA1.2.473244792.1479120598","D_PID":"1AEE13A2-C955-30B6-B8E3-3EF40A8E9B22","D_IID":"EF14F1DA-9446-3019-A32C-1B8C0D8FADA1","D_UID":"AE5459A6-F3D4-3291-9EB2-BC3BA8EDC481","D_HID":"YDUhwlw5ts0955n4/+XxkGf++Zyfsrb5k/Gy7asKpnw","D_ZID":"574A8A1D-B06F-3434-934E-3DA6207F28A6","D_ZUID":"66E3926B-08FA-38A2-9416-98B29C7CA7A1","utag_main":"v_id:01586275256c00867fe7817bb9100506c002a064006c4$_sn:6$_ss:0$_st:1479192712865$dc_visit:6$ses_id:1479189508434%3Bexp-session$_pn:9%3Bexp-session$dc_event:17%3Bexp-session$dc_region:eu-central-1%3Bexp-session","com.silverpop.iMAWebCookie":"24b2467a-7822-d653-b5e3-0e7c36c4da0e","com.silverpop.iMA.page_visit":"-1414739851,-675724828,1794053400,-1514207638,","com.silverpop.iMA.session":"d91550dd-35e9-b652-05c1-a1e5647b0c0d","_bizo_bzid":"9f01d843-de30-4d47-a403-d814a230159f","_bizo_cksm":"D7DB8BA74C9FC259","_bizo_np_stats":"14%3D274%2C","optimizelyPendingLogEvents":"%5B%5D","_gali":"Book_Flight","__CG":"u%3A5054936325467030000%2Cs%3A398593949%2Ct%3A1479190927266%2Cc%3A9%2Ck%3Abook.cathaypacific.com/152/152/5913%2Cf%3A0%2Ci%3A1"}
    url="https://book.cathaypacific.com/pl/CathayPacificV2/wds/OverrideServlet;jsessionid=DJlnGavZ7LkfQ2-tuPp6K2jCmQFfd389Qc_wQmMfqLccItpuPLH9!17004718!87143942"
    #dat={"EMBEDDED_TRANSACTION":"AddElementsServlet","LANGUAGE":"CN","SITE":"CBERCBER","CABIN":"M","PAGE_TICKET":"2","TYPE":"AIR_TRIP_FARE","WDS_MILES_EARNED_STR":"161120162215%2C161120162320%2C171120160900%2C171120161300CX%2CCXKA%2CCX5789%2C759L%2CLCAN%2CHKG%2CHKG%2CSIN16760150","WDS_CLUBPOINTS_EARNED_STR":"","WDS_OFFSET_CARBON_STR":"","WDS_SEAT_STR":"161120162215%2C161120162320%2C171120160900%2C171120161300CX%2CCX5789%2C759L%2CLCAN%2CHKG%2CHKG%2CSINtruetrue","WDS_MILES_EARNED_CHECKSUM":"9685C391758DED8A3BDAE7360F47CBD8","WDS_OFFSET_CARBON_CHECKSUM":"","WDS_SEAT_CHECKSUM":"9E8270038C16E3066EAE32F66941A65B","WDS_MILES_RESPONSE":"earnedMiles%3D1676%3AbonusMiles%3D0%3AbonusMilesLink%3D%3AaAdvantageEligible%3Dfalse%3AtotalMiles%3D1676%3AearnedPoints%3D15%3AbonusPoints%3D0%3AbonusPointsLink%3D%3APointsaAdvantageEligible%3Dfalse%3AtotalPoints%3D15","WDS_CLUBPOINTS_RESPONSE":"","WDS_CARBON_RESPONSE":"","WDS_SEATS_RESPONSE":"SEAT_0_0%3Dtrue%3ASEAT_0_1%3Dtrue","FIRST_PAGE":"FFCL","MINI_RULES_AJAX_SUCCESS":"true","SERVICE_POLICY_AJAX_SUCCESS":"true","CONVERT_CURRENCY":"NO","WDS_CARBON_RADIO":"FALSE","LATE_LOGIN":"FALSE","LOGIN":"","PASSWORD":""}
    dat={"EMBEDDED_TRANSACTION":"AddElementsServlet","LANGUAGE":"CN","SITE":"CBERCBER","CABIN":"M","PAGE_TICKET":"2","TYPE":"AIR_TRIP_FARE","WDS_MILES_EARNED_STR":"161120160950%2C161120161100%2C171120160810%2C171120161155CX%2CCXKA%2CCX5783%2C691L%2CLCAN%2CHKG%2CHKG%2CSIN16760150","WDS_CLUBPOINTS_EARNED_STR":"","WDS_OFFSET_CARBON_STR":"","WDS_SEAT_STR":"161120160950%2C161120161100%2C171120160810%2C171120161155CX%2CCX5783%2C691L%2CLCAN%2CHKG%2CHKG%2CSINtruetrue","WDS_MILES_EARNED_CHECKSUM":"11EE232F1F35C04FAAD73AB6162800C3","WDS_OFFSET_CARBON_CHECKSUM":"","WDS_SEAT_CHECKSUM":"1D320654FD9261A880725768948F9F84","WDS_MILES_RESPONSE":"earnedMiles%3D1676%3AbonusMiles%3D0%3AbonusMilesLink%3D%3AaAdvantageEligible%3Dfalse%3AtotalMiles%3D1676%3AearnedPoints%3D15%3AbonusPoints%3D0%3AbonusPointsLink%3D%3APointsaAdvantageEligible%3Dfalse%3AtotalPoints%3D15","WDS_CLUBPOINTS_RESPONSE":"","WDS_CARBON_RESPONSE":"","WDS_SEATS_RESPONSE":"SEAT_0_0%3Dtrue%3ASEAT_0_1%3Dtrue","FIRST_PAGE":"FFCL","MINI_RULES_AJAX_SUCCESS":"true","SERVICE_POLICY_AJAX_SUCCESS":"true","CONVERT_CURRENCY":"NO","WDS_CARBON_RADIO":"FALSE","LATE_LOGIN":"FALSE","LOGIN":"","PASSWORD":""}
    page = request_page(url,dat)
    return page

if __name__=='__main__':


    #result=html.xpath('/html/body//tbody[@id="mainTabContent"]/tr//*')
    #r=result
    #r=person_info()
    t=get_fares()


