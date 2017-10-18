# -*- coding: utf-8 -*-
import scrapy
import json
import os
from aiss.items import AissItem
# http://com-pmkoo-img.oss-cn-beijing.aliyuncs.com/header/XiaMo.jpg
def save_page(page_json):
    """ 保存某页面的信息 """
    txt = json.dumps(page_json)

    with open('data.txt', 'w') as f:
        f.write(txt)
        f.write('\n')

def get_info_imgs(info):
    """ 获取要下载的所有图片url、目录名、要存储的名字 """
    items = []

    for i in info:
        item = {}
        item['author'] = i["author"]["nickname"]
        item['catalog'] = i["source"]["catalog"]
        item['source'] = i["source"]["name"]
        item['issue'] = i["issue"]
        item['count'] = i["pictureCount"]
        item['image_urls'] = []
    
        for pic_idx in range(i["pictureCount"]):
            # http://com-wuwei-aiss.oss-cn-beijing.aliyuncs.com/picture/xiuren/232/21.jpg
            url = "http://com-wuwei-aiss.oss-cn-beijing.aliyuncs.com/picture/%s/%s/%s.jpg" % (item['catalog'], item['issue'], pic_idx)
            item['image_urls'].append(url)
        
        items.append(item)

    return items

class MmSpider(scrapy.Spider):
    allowed_domains = ['pmkoo.cn']
    start_urls = ['http://api.pmkoo.cn/']
    params = {'page': '13', 'userId': '153044'}
    name = 'mm'
    url = 'http://api.pmkoo.cn/aiss/suite/suiteList.do'

    def parse(self, response):
        yield scrapy.FormRequest(url=self.url, formdata=self.params, callback=self.after_login)

    def after_login(self, response):
        item = json.loads(response.body_as_unicode())
        info = item['data'].get('list')

        if info:
            rows = get_info_imgs(info)
            
            for row in rows:
                aiss = AissItem()            
                aiss.update(row)

                yield aiss

            self.params['page'] = str(int(self.params['page']) + 1)
            yield scrapy.FormRequest(url=self.url, formdata=self.params, callback=self.after_login)

        
          
