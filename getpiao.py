#!-*- coding:utf-8 -*-
__author__ = 'Administrator'
import requests
#import urllib2
#import urllib
import re
import datetime
from lxml import etree
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
    ret=s.post(url, data=dat)
    return ret

#获取今后的第n天
def getndate(n):
    return (datetime.date.today() + datetime.timedelta(days=n)).strftime("%Y%m%d")

#获取时间戳
def GetTimeStamp():
    return datetime.datetime.now().strftime("%d%m%Y%H%M")

def get_fares():
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
    ret1=request_page(url1,dat1)
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
    url2="https://book.cathaypacific.com/pl/CathayPacificV2/wds/FlexPricerAvailabilityServlet;"
    url2=url2+jsessionid
    dat2={"LANGUAGE":"CN","SITE":"CBERCBER","TRIP_FLOW":"YES","SKIN":"CX",
          "EXTERNAL_ID":"0000I26d1yJv4iBjOPwGdAPxJCS%3A-1","COUNTRY":"CN","FROM_SITE":"CX",
          "B_LOCATION_2":"","B_LOCATION_1":"CAN","E_LOCATION_2":"","E_LOCATION_1":"SIN",
          "B_DATE_1":"201611100000","B_DATE_2":"","TRAVELLER_TYPE_1":"ADT","HAS_INFANT_1":"",
          "TRAVELLER_TYPE_2":"","HAS_INFANT_2":"","TRAVELLER_TYPE_3":"","HAS_INFANT_3":"",
          "TRAVELLER_TYPE_4":"","HAS_INFANT_4":"","TRAVELLER_TYPE_5":"","HAS_INFANT_5":"",
          "TRAVELLER_TYPE_6":"","HAS_INFANT_6":"","TRAVELLER_TYPE_7":"","HAS_INFANT_7":"",
          "TRAVELLER_TYPE_8":"","HAS_INFANT_8":"","TRAVELLER_TYPE_9":"","HAS_INFANT_9":"",
          "TRIP_TYPE":"O","COMMERCIAL_FARE_FAMILY_1":"CFFECO","COMMERCIAL_FARE_FAMILY_2":"",
          "COMMERCIAL_FARE_FAMILY_3":"","DIRECT_NON_STOP":"","PRICING_TYPE":"I","DISPLAY_TYPE":"1",
          "WDS_METHODS_OF_PAYMENT":"CREDITCARD","WDS_METHODS_OF_DELIVERY":"ETCKT",
          "WDS_MOD_DESC_AIRL":"","WDS_MOD_DESC_DELIV":"","WDS_MOD_DESC_ETCKT":"e-Ticket",
          "WDS_MOD_DESC_HAND":"","WDS_MOD_DESC_PICK":"","WDS_INCLUDE_TAX":"FALSE",
          "WDS_PROPOSE_UPSELL":"TRUE","WDS_NEXT_CABIN":"","WDS_FROM_CALENDAR":"TRUE",
          "FIRST_PAGE":"FFCL","PROMO_CODE":"","CALENDAR_PRICE_SELECTED":"",
          "WDS_DATE":"201611100000"}
    #选择日期
    dat2.update({
        "B_DATE_1":dat1["B_DATE_1"],#"201611100000",
        "WDS_DATE":dat1["B_DATE_1"],#"201611100000"
    })
    ret2=request_page(url2,dat2)
    if ret2.ok:
        txt=ret2.content
    else:
        txt=""
    html=etree.HTML(txt)
    print u"获取到第二个页面"
    #result=html.xpath('//*[@class="first"]')
    #看票价
    charge=html.xpath('//*[@name="WDS_GROUP"][@value="CANECOSRSALowest"]//span[2]') #票价

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
    ret3=request_page(url3,dat3)
    dat3f={"BACKUP_TO_FULL_RULES":"true","RULE_SOURCE_1_TYPE":"FARE","RULE_SOURCE_1_ID":"","FROM_FLOW_TRANSACTION":"","FROM_FLOW_INITIAL_PRODUCT":"","FROM_FLOW_BOOKING_TYPE":"","FROM_FLOW_FEATURE_1_CODE":"",}
    dat3f.update({
        "LANGUAGE":"CN",
        "TRANSACTION_ID":"MiniRules",
        "JSESSION_ID":jsessionid[11:],
        "SITE":"CBERCBER",})
    url3f="https://book.cathaypacific.com/pl/CathayPacificV2/wds/MiniRulesServlet;"+jsessionid
    ret3f=request_page(url3f,dat3f)

    #生成订单添加元素
    url4="https://book.cathaypacific.com/pl/CathayPacificV2/wds/AddElementsServlet;"
    url4=url4+jsessionid
    dat4={"SITE","CBERCBER","LANGUAGE","CN","PAGE_TICKET","3","FROM_PAX","TRUE","DELIVERY_TYPE","ETCKT","NB_ADT","1","NB_CHD","0","NB_INF","0","Dyc_EMAI","%3Cdiv+class%3D%22dync_content%22%3E+++++++++%3Ch2+style%3D%22color%3A%23006564%3Bmargin%3A+10px+0+10px+0%3B+font-family%3AAktiv+Grotesk+W01+Regular%2CArial%2CHelvetica%2CSans-serif%3B+font-size%3A+1.45em%3B+font-weight%3A+300%3B+text-align%3A+left%3B%22%3E%E6%97%85%E6%B8%B8%E6%8F%90%E7%A4%BA%3C%2Fh2%3E+++%3Cdiv+style%3D%22width%3A190px%3Bfloat%3Aleft%3Bmargin%3A5px%22%3E%3Ca+class%3D%22right-arrow-icon%22+style%3D%22color%3A%230f7e92%3Bline-height%3A23px%3Btext-decoration%3Anone%3B%22+target%3D%22_blank%22+href%3D%22https%3A%2F%2Fwww.cathaypacific.com%2Fcx%2Fsc_CN%2Fmanage-booking.html%3Futm_channel%3DEDM%26amp%3Butm_source%3DCX_SERVICES%26amp%3Butm_medium%3DIBE_REV_CONF%26amp%3Butm_campaign%3DMMB%26amp%3Butm_content%3DMMB%26amp%3Butm_term%3DFOOTER%22%3E%E7%AE%A1%E7%90%86%E8%A1%8C%E7%A8%8B%3C%2Fa%3E%3C%2Fdiv%3E%3Cdiv+style%3D%22width%3A190px%3Bfloat%3Aleft%3Bmargin%3A5px%22%3E%3Ca+class%3D%22right-arrow-icon%22+style%3D%22color%3A%230f7e92%3Bline-height%3A23px%3Btext-decoration%3Anone%3B%22+target%3D%22_blank%22+href%3D%22https%3A%2F%2Fwww.cathaypacific.com%2Fcx%2Fsc_CN%2Fabout-us%2Fcontact-us%2Ffaqs%2Fonline-booking-ticket-purchase%2Fchanges-cancellation-and-refund.html%3Futm_channel%3DEDM%26amp%3Butm_source%3DCX_SERVICES%26amp%3Butm_medium%3DIBE_REV_CONF%26amp%3Butm_campaign%3DCHANGE-BOOKING%26amp%3Butm_content%3DFAQ%26amp%3Butm_term%3DFOOTER%22%3E%E6%9B%B4%E6%94%B9%E8%AE%A2%E7%A5%A8%3C%2Fa%3E%3C%2Fdiv%3E%3Cdiv+style%3D%22width%3A190px%3Bfloat%3Aleft%3Bmargin%3A5px%22%3E%3Ca+class%3D%22right-arrow-icon%22+style%3D%22color%3A%230f7e92%3Bline-height%3A23px%3Btext-decoration%3Anone%3B%22+target%3D%22_blank%22+href%3D%22https%3A%2F%2Fwww.cathaypacific.com%2Fcx%2Fsc_CN%2Ftravel-information%2Ftravel-preparation%2Fvisa-information%2Fpassport-visa-information.html%3Futm_channel%3DEDM%26amp%3Butm_source%3DCX_SERVICES%26amp%3Butm_medium%3DIBE_REV_CONF%26amp%3Butm_campaign%3DVISA-INFORMATION%26amp%3Butm_content%3DTRAVEL-INFORMATION%26amp%3Butm_term%3DFOOTER%22%3E%E6%8A%A4%E7%85%A7%E7%AD%BE%E8%AF%81%E8%B5%84%E8%AE%AF%3C%2Fa%3E%3C%2Fdiv%3E%3Cdiv+style%3D%22width%3A190px%3Bfloat%3Aleft%3Bmargin%3A5px%22%3E%3Ca+class%3D%22right-arrow-icon%22+style%3D%22color%3A%230f7e92%3Bline-height%3A23px%3Btext-decoration%3Anone%3B%22+target%3D%22_blank%22+href%3D%22https%3A%2F%2Fwww.cathaypacific.com%2Fcx%2Fsc_CN%2Fmanage-booking%2Fcheck-in.html%3Futm_channel%3DEDM%26amp%3Butm_source%3DCX_SERVICES%26amp%3Butm_medium%3DIBE_REV_CONF%26amp%3Butm_campaign%3DOLCI%26amp%3Butm_content%3DOLCI%26amp%3Butm_term%3DFOOTER%22%3E%E7%BD%91%E4%B8%8A%E9%A2%84%E5%8A%9E%E7%99%BB%E6%9C%BA%3C%2Fa%3E%3C%2Fdiv%3E%3Cdiv+style%3D%22width%3A190px%3Bfloat%3Aleft%3Bmargin%3A5px%22%3E%3Ca+class%3D%22right-arrow-icon%22+style%3D%22color%3A%230f7e92%3Bline-height%3A23px%3Btext-decoration%3Anone%3B%22+target%3D%22_blank%22+href%3D%22https%3A%2F%2Fitunes.apple.com%2Fau%2Fapp%2Fcx-discovery%2Fid545892116%3Fmt%3D8%22%3EDiscovery+%E8%88%AA%E7%A9%BA%E6%9D%82%E5%BF%97%3C%2Fa%3E%3C%2Fdiv%3E%3Cdiv+style%3D%22width%3A190px%3Bfloat%3Aleft%3Bmargin%3A5px%22%3E%3Ca+class%3D%22right-arrow-icon%22+style%3D%22color%3A%230f7e92%3Bline-height%3A23px%3Btext-decoration%3Anone%3B%22+target%3D%22_blank%22+href%3D%22https%3A%2F%2Fwww.cathaypacific.com%2Fcx%2Fsc_CN%2Ftravel-information%2Fairport.html%3Futm_channel%3DEDM%26amp%3Butm_source%3DCX_SERVICES%26amp%3Butm_medium%3DIBE_REV_CONF%26amp%3Butm_campaign%3DAIRPORT-INFOMRATION%26amp%3Butm_content%3DTRAVEL-INFORMARTION%26amp%3Butm_term%3DFOOTER+%22%3E%E6%9C%BA%E5%9C%BA%E8%B5%84%E6%96%99%3C%2Fa%3E%3C%2Fdiv%3E+++%3Cbr+style%3D%22clear%3Aboth%22%3E+++%3Cp+style%3D%22color%3A%234c4c4c%3Bfont-family%3AAktiv+Grotesk+W01+Regular%2CArial%2CHelvetica%2CSans-serif%3B%22%3E%E6%88%96%E8%81%94%E7%B3%BB+%3Ca+target%3D%22_blank%22+style%3D%22color%3A%230f7e92%3Btext-decoration%3Anone%3B%22+href%3D%22https%3A%2F%2Fwww.cathaypacific.com%2Fcx%2Fsc_CN%2Fabout-us%2Fcontact-us%2Fglobal-contact-centres.html%3Futm_channel%3DEDM%26amp%3Butm_source%3DCX_SERVICES%26amp%3Butm_medium%3DIBE_REV_CONF%26amp%3Butm_campaign%3DCONTACT-GCC%26amp%3Butm_content%3DCONTACT-US%26amp%3Butm_term%3DFOOTER%22%3E%E5%85%A8%E7%90%83%E5%AE%A2%E6%88%B7%E6%9C%8D%E5%8A%A1%E4%B8%AD%E5%BF%83%3C%2Fa%3E%3C%2Fp%3E+++%3C%2Fdiv%3E","Dyc_EMAI_2","","Dyc_EMAI_BOH","","DycTerms_EMAI","","WDS_ALPI","TRUE","POPIN_CANCEL","","CONTACT_POINT_HOME_PHONE_OC","","CONTACT_POINT_HOME_PHONE_AC","","CONTACT_POINT_BUSINESS_PHONE_OC","","CONTACT_POINT_BUSINESS_PHONE_AC","","CONTACT_POINT_MOBILE_1_OC","","CONTACT_POINT_MOBILE_1_AC","","NOTIF_TYPE_1_1","E","NOTIF_VALUE_1_1","2231686756%40qq.com","NOTIF_TYPE_1_2","M","NOTIF_VALUE_1_2","15671532758","NOTIF_OVERSEAS_CODE_1_2","86","WDS_CREDITCARD_LIST","","WDS_DEBITCARD_LIST","CU","PSP_LIST","adyen%2Cbtb","WDS_VI","","WDS_CA","","WDS_AX","","WDS_TP","","WDS_DC","","WDS_JC","","Dyc_PURC_msg","","Dyc_PURC_display","","WDS_FXMPCARD_LIST","VI%3ACA","IDENTITY_DOCUMENT_GENDER_PSPT_0","","IDENTITY_DOCUMENT_NATIONALITY_PSPT_0","","IDENTITY_DOCUMENT_DATE_OF_BIRTH_PSPT_0","","IDENTITY_DOCUMENT_LAST_NAME_PSPT_0","","IDENTITY_DOCUMENT_FIRST_NAME_PSPT_0","","IDENTITY_DOCUMENT_MIDDLE_NAME_PSPT_0","","IDENTITY_DOCUMENT_TYPE_PSPT_0","","IDENTITY_DOCUMENT_NUMBER_PSPT_0","","IDENTITY_DOCUMENT_ISSUING_COUNTRY_PSPT_0","","IDENTITY_DOCUMENT_EXPIRY_DATE_PSPT_0","","IDENTITY_DOCUMENT_TYPE_VISA_0","","IDENTITY_DOCUMENT_NUMBER_VISA_0","","IDENTITY_PLACE_OF_ISSUING_VISA_0","","IDENTITY_DOCUMENT_ISSUE_DATE_VISA_0","","IDENTITY_DOCUMENT_APPLICABLE_COUNTRY_VISA_0","","IDENTITY_DOCUMENT_PLACE_OF_BIRTH_VISA_0","","APIS_ADDRESS_FIRSTLINE_R_0","","APIS_ADDRESS_SECONDLINE_R_0","","APIS_ADDRESS_CITY_R_0","","APIS_ADDRESS_ZIPCODE_R_0","","APIS_ADDRESS_STATE_R_0","","APIS_ADDRESS_COUNTRY_R_0","","APIS_ADDRESS_FIRSTLINE_D_0","","APIS_ADDRESS_SECONDLINE_D_0","","APIS_ADDRESS_CITY_D_0","","APIS_ADDRESS_ZIPCODE_D_0","","APIS_ADDRESS_STATE_D_0","","APIS_ADDRESS_COUNTRY_D_0","","DATE_OF_BIRTH_DAY_0","","DATE_OF_BIRTH_MONTH_0","","DATE_OF_BIRTH_YEAR_0","","DATE_OF_EXPIRATION_DAY_0","","DATE_OF_EXPIRATION_MONTH_0","","DATE_OF_EXPIRATION_YEAR_0","","DATE_OF_ISSUE_DAY_0","","DATE_OF_ISSUE_MONTH_0","","DATE_OF_ISSUE_YEAR_0","","SELECT_TITLE_1","MR","TITLE_1","MR","LAST_NAME_1","wan","FIRST_NAME_1","ci","FIRST_FF_AIRLINE","","PREF_AIR_FREQ_AIRLINE_1_1","","PREF_AIR_FREQ_NUMBER_1_1","","CONTACT_POINT_EMAIL_1","2231686756%40qq.com","CONTACT_POINT_HOME_PHONE","86-15671532758","CONTACT_POINT_MOBILE","86-15671532758","CONTACT_POINT_BUSINESS_PHONE","","PHONE_TYPE","MOB","PHONE_COUNTRY","86","PHONE_AREA","","PHONE_NUMBER","15671532758","ALPI_PREF_AIR_MEAL_1","STRD","AM_adtDateOfBirthDay1","","AM_adtDateOfBirthMonth1","","AM_adtDateOfBirthYear1","","IDENTITY_DOCUMENT_NATIONALITY_PSPT_AM","","enrolment_total","","enrolment_success","","AM_notSuccessful_TravellerIDs","","AM_call_failure","","AM_TravellerID_to_FFN_Mapping","","AM_ENROLMENT_SELECTED","","REGISTRATION_STATUS","","REGISTRATION_RESPONSE_CODE","","PREF_AIR_SEAT_ASSIGMENT_1_1","","PREF_AIR_SEAT_ASSIGMENT_1_2",""}
    #ret4=request_page(url4,dat4)
    return ret3


if __name__=='__main__':
    t=get_fares()








