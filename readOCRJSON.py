# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:08:50 2022

@author: vincentkuo
"""


import json
import re
from dateutil.parser import parse
from datetime import date

dataLoc = 'D:\\下載\\Sample\\invoice-longstrip\\TestResult\\fake4.jpg.labels.json'
dataLocList = ['D:\\下載\\Sample\\invoice-longstrip\\TestResult\\fake2.jpg.labels.json',
               'D:\\下載\\Sample\\invoice-longstrip\\TestResult\\fake4.jpg.labels.json',
               'D:\\下載\\Sample\\invoice-longstrip\\TestResult\\fake6.jpg.labels.json',
               'D:\\下載\\Sample\\invoice-longstrip\\TestResult\\S10.jpg.labels.json',
               'D:\\下載\\Sample\\invoice-longstrip\\TestResult\\S10_2.jpg.labels.json',
               'D:\\下載\\Sample\\invoice-longstrip\\TestResult\\H5.PNG.labels.json',
               'D:\\下載\\Sample\\invoice-longstrip\\TestResult\\H6.PNG.labels.json',
               'D:\\下載\\Sample\\invoice-longstrip\\TestResult\\IMG_20220121_101353.jpg.labels.json']

#dataLocList = ['D:\\下載\\Sample\\invoice-triple\\TestResult\\E4.jpg.labels.json',
#               'D:\\下載\\Sample\\invoice-triple\\TestResult\\E4_400.png.labels.json',
#               'D:\\下載\\Sample\\invoice-triple\\TestResult\\E5.jpg.labels.json',
#               'D:\\下載\\Sample\\invoice-triple\\TestResult\\Fake4.jpg.labels.json',
#               'D:\\下載\\Sample\\invoice-triple\\TestResult\\Fake5.jpg.labels.json',
#               'D:\\下載\\Sample\\invoice-triple\\TestResult\\Fake7.jpg.labels.json',
#               'D:\\下載\\Sample\\invoice-triple\\TestResult\\Fake8.jpg.labels.json',
#               'D:\\下載\\Sample\\invoice-triple\\TestResult\\S1.jpg.labels.json']

# dataLocList = ['D:\\下載\\Sample\\invoice-cashier\\TestResult\\J4.jpg.labels.json',
#                'D:\\下載\\Sample\\invoice-cashier\\TestResult\\J5.jpg.labels.json',
#                'D:\\下載\\Sample\\invoice-cashier\\TestResult\\S14.jpg.labels.json',
#                'D:\\下載\\Sample\\invoice-cashier\\TestResult\\fake2.jpg.labels.json']

# dataLocList = ['D:\\下載\\Sample\\invoice-ecalculator\\TestResult\\I2.jpg.labels.json',
#                'D:\\下載\\Sample\\invoice-ecalculator\\TestResult\\I5.pdf.labels.json',
#                'D:\\下載\\Sample\\invoice-ecalculator\\TestResult\\S13.jpg.labels.json',
#                'D:\\下載\\Sample\\invoice-ecalculator\\TestResult\\fake2.jpg.labels.json']

def is_date(string, fuzzy=True):
    try:
        if '國' in string or '年' in string:
            return 'E'
        parse(string, fuzzy=fuzzy)
        return parse(string, fuzzy=fuzzy)
    except ValueError:
        return 'E'

def isValidDate(yy,mm,dd):
    try:
        date(int(yy),int(mm),int(dd))
    except:
        return False
    else:
        return True

def validYYMMDD(yy,mm,dd):
    try:
        if isValidDate(yy,mm,dd):
            if int(yy)<1911:
                yy+=1911
            return yy,mm,dd
        else:
            return False,False,False
    except:
        print('YYMMDD ERROR')
        return False,False,False

def validInvoiceNum(value):
    try:
        num = re.compile('[A-Z]\s*[A-Z]\s*\d\s*\d\s*\d\s*\d\s*\d\s*\d\s*\d\s*\d')
        
    except:
        print('Invoice Num Error')
    return ';'.join(num.findall(value))

def validTaxNum(value):
    try:
        num = re.compile('[\#]*\d\s*\d\s*\d\s*\d\s*\d\s*\d\s*\d\s*\d')
        if len(num.findall(value))==2:
            for i in num.findall(value):
                if '#' in i:
                    return i.replace('#','')
        
    except:
        print('Invoice Num Error')
    return ';'.join(num.findall(value))

def validDate(value):
    try:
        case1 = re.compile('[\u570b]\s*\d\s*\d\s*\d*\s*\d*\s*[\u5e74]\s*\d\s*\d*\s*[\u6708]*\s*\d\s*\d*')
        case2 = re.compile('\d\s*\d\s*\d\s*\d\s*[\-\/]\s*\d\s*\d*\s*[\-\/]\s*\d{1,2}')

        # Case 1 國 yy 年 mm 月 dd 日
        if len(case1.findall(value))==1:
            yy = int(case1.findall(value)[0].replace('國','').replace('年','-').replace('月','-').split('-')[0])
            mm = int(case1.findall(value)[0].replace('國','').replace('年','-').replace('月','-').split('-')[1])
            dd = int(case1.findall(value)[0].replace('國','').replace('年','-').replace('月','-').split('-')[2])
            yy,mm,dd = validYYMMDD(yy,mm,dd) # 民國日期格式調整
        elif len(case1.findall(value))>1:
            yy = int(case1.findall(value)[0].replace('國','').replace('年','-').replace('月','-').split('-')[0])
            mm = int(case1.findall(value)[0].replace('國','').replace('年','-').replace('月','-').split('-')[1])
            dd = int(case1.findall(value)[0].replace('國','').replace('年','-').replace('月','-').split('-')[2])
            yy,mm,dd = validYYMMDD(yy,mm,dd) # 民國日期格式調整
            if yy or mm or dd == False:
                yy = int(case1.findall(value)[1].replace('國','').replace('年','-').replace('月','-').split('-')[0])
                mm = int(case1.findall(value)[1].replace('國','').replace('年','-').replace('月','-').split('-')[1])
                dd = int(case1.findall(value)[1].replace('國','').replace('年','-').replace('月','-').split('-')[2])
                yy,mm,dd = validYYMMDD(yy,mm,dd) # 民國日期格式調整
        # Case 2 直接可編譯
        elif is_date(value)!='E':
            yy = is_date(value).year
            mm = is_date(value).month
            dd = is_date(value).day
            yy,mm,dd = validYYMMDD(yy,mm,dd) # 民國日期格式調整
        # Case 3 yyyy-mm-dd or yyyy/mm/dd
        elif len(case2.findall(value))==1:
            if is_date(case2.findall(value)[0])!='E':
                yy = is_date(case2.findall(value)[0]).year
                mm = is_date(case2.findall(value)[0]).month
                dd = is_date(case2.findall(value)[0]).day
                yy,mm,dd = validYYMMDD(yy,mm,dd) # 民國日期格式調整
            else:
                yy = int(case2.findall(value)[0].replace('/','-').split('-')[0])
                mm = int(case2.findall(value)[0].replace('/','-').split('-')[1])
                dd = int(case2.findall(value)[0].replace('/','-').split('-')[2])
                yy,mm,dd = validYYMMDD(yy,mm,dd) # 民國日期格式調整
        elif len(case2.findall(value))>1:
            if is_date(case2.findall(value)[0])!='E':
                yy = is_date(case2.findall(value)[0]).year
                mm = is_date(case2.findall(value)[0]).month
                dd = is_date(case2.findall(value)[0]).day
                yy,mm,dd = validYYMMDD(yy,mm,dd) # 民國日期格式調整
            elif is_date(case2.findall(value)[1])!='E':
                yy = is_date(case2.findall(value)[1]).year
                mm = is_date(case2.findall(value)[1]).month
                dd = is_date(case2.findall(value)[1]).day
                yy,mm,dd = validYYMMDD(yy,mm,dd) # 民國日期格式調整
            else:
                yy = int(case2.findall(value)[0].replace('/','-').split('-')[0])
                mm = int(case2.findall(value)[0].replace('/','-').split('-')[1])
                dd = int(case2.findall(value)[0].replace('/','-').split('-')[2])
                yy,mm,dd = validYYMMDD(yy,mm,dd) # 民國日期格式調整
                if (yy or mm or dd) == False:
                    yy = int(case2.findall(value)[1].replace('/','-').split('-')[0])
                    mm = int(case2.findall(value)[1].replace('/','-').split('-')[1])
                    dd = int(case2.findall(value)[1].replace('/','-').split('-')[2])
                    yy,mm,dd = validYYMMDD(yy,mm,dd) # 民國日期格式調整
        if (yy or mm or dd) == False:
            value = ''
        else:  
            value = str(yy)+','+str(mm)+','+str(dd)
    except:
        print('Date Format Error')
        return ''
    return value


def getValue(data):
    try:
        value=''
        length = len(data)
        for i in range(length):
            value += data[i]['text']
    except:
        print('Something error')
    return value

for data in dataLocList:
    with open(data,'r', encoding='utf-8') as f:
        data = json.load(f)
        tempArray = []
        tempArrayAdjusted = []
        length = len(data['labels'])
        for i in range(length):
            key = data['labels'][i]['label']
            value = getValue(data['labels'][i]['value'])
            tempArray.append({key:value})
            
            if key=='發票號碼':
                value = validInvoiceNum(value)
                if len(value)<10:
                    value = ''
            if key=='統一編號賣方' or key=='統一編號買家' or key=='統一編號買方':
                value = validTaxNum(value)
                if len(value)<8:
                    value = ''
            if key=='日期':
                value = validDate(value)
            tempArrayAdjusted.append({key:value})
    
    print('###############################################################')
    print(tempArray)
    print(tempArrayAdjusted)