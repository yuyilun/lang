__author__ = 'CQC'
# -*- coding:utf-8 -*-

import urllib
import urllib2
import re

class Spider:

    def __init__(self):
        self.siteURL = 'https://mm.taobao.com/search_tstar_model.htm'

    def getPage(self,pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')

    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        print page
        pattern = re.compile('<li class="item".*?<a href="(.*?)".*?<img src="(.*?)".*?<span class="name">(.*?)</span>.*?<span class="city">(.*?)</span>.*?<span>(.*?)</span>',re.S)

        items = re.findall(pattern,page)
        print items
        for item in items:
            print item[0],item[1],item[2],item[3],item[4]
            
spider = Spider()
spider.getContents(1)
