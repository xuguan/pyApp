# -*- coding: cp936 -*-
# -*- coding: gb18030 -*- 
# -*- coding: utf-8 -*-

#�������ѯ�����ѣ�pycurl��ȡ��ַ��Ӧ��json��ʽ���ݣ�body.index('string')Ѱ�����ǹ��ĵ��ַ������õ�������urllib��xml���Լ�StringIO����

import pycurl
import urllib
import xml.dom.minidom
from StringIO import StringIO

buffer=StringIO()
c=pycurl.Curl()
c.setopt(pycurl.POST,1)
#The head field can be abstracted from the tcp streaming tools of a wireshark,
#when you lookup the url from browser.
head=['Host: 172.19.53.245',
    'Connection: keep-alive',
    'Content-Length: 79',
    'Origin: http://172.19.53.245',
    'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 BIDUBrowser/7.6 Safari/537.36',
    'Content-Type: application/json; charset=UTF-8',
    'Accept: */*',
    'Referer: http://172.19.53.245/selectPage.aspx',
    'Accept-Encoding: gzip, deflate',
    'Accept-Language: zh-CN,zh;q=0.8',
    'DNT: 1'
      ]
c.setopt(c.HTTPHEADER, head)
c.setopt(c.URL, 'http://172.19.53.245/selectPage.aspx/SerBindTabDate')
post_json_data='{"nodeInText":"11537*Meter*...3-913*001401079330","PartList":"","SelectPart":1}'
c.setopt(c.POSTFIELDS, post_json_data)
c.setopt(c.WRITEFUNCTION, buffer.write)
c.perform()
c.close()
body=buffer.getvalue()
#print body

title_index=body.index('"d":"')
title=body[title_index+5:title_index+70]
print title.decode('utf-8')

syvalue_index=body.index("tdSYValue")
#print syvalue_index
syvalue=body[syvalue_index+21:syvalue_index+33]
print "1. ʣ�������"
print syvalue.decode('utf-8')

tdValueTime_index=body.index("tdValueTime")
tdValueTime=body[tdValueTime_index+23:tdValueTime_index+42]
print "2. ����ʱ��"
print tdValueTime.decode('utf-8')

#text = '1��'
#text = unicode( text, 'gbk' ).encode( 'gb18030' )
#text_index=body.index(text)
#print text.decode('gbk')

## ���н������
##
##>>> 
##���пƼ���ѧ.��ʿ����Ԣ.��ʿ����Ԣ����.��3-913
##1. ʣ�������
##86.53��\u00
##2. ����ʱ��
##2016/7/13 11:37:04\
##>>> 
