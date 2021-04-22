# -*- coding: utf-8 -*-
import scrapy
from SpiderForbes.items import SpiderforbesItem, ItemEncoder
import json
import pandas as pd

class ForbesSpider(scrapy.Spider):
    name = 'forbes'
    allowed_domains = ['forbes.com']
    start_urls = ['https://www.forbes.com/business']



    def parse(self, response):

        i = 1

        article_list = response.xpath('//*[@id="row-2"]/div/div/div/div[1]/div/div/article')

        for article in article_list:
            item = SpiderforbesItem()
            item["num"] = i
            item["title"] = article.xpath('./div[1]/h2/a/text()').extract_first()
            item["url"] = article.xpath('./div[1]/h2/a/@href').extract_first()
            item["description"] = article.xpath('./div[1]/div[2]/text()').extract_first()
            item["author"] = article.xpath('./div[1]/div[3]/span/div/div/a/text()').extract_first()
            # author_type = article.xpath('./div[1]/div[3]/span/div/div/span[2]/text()').extract_first()


            yield scrapy.Request(item["url"], callback=self.parse_detail, meta={"item":item})

            i += 1



    def parse_detail(self, response):
        item = response.meta["item"]
        num = item["num"]
        # content = response.xpath('//*[@id="article-stream-0"]/div[2]/div[2]/div[3]/div[1]/p')
        # content = response.xpath('//*[@id="article-stream-0"]/div[2]/div[2]/div[3]/div[1]/p/text()')

        # for paragraph in content:
        #     if paragraph.xpath('./text()').extract_first() is not None:
        #         article = paragraph.xpath('./text()').extract_first()
        #     for spa in paragraph.xpath('./span'):
        #         # if spa.extract_first() is not None:
        #         article = article + ' ' + spa.extract_first()
        item["content"] = response.xpath('//*[@id="article-stream-0"]/div[2]/div[2]/div[3]/div[1]/p/text()').extract()
        # print(item["content"])

        item = ItemEncoder().encode(item)

        jsObj = json.dumps(item)

        fileObject = open(str(num)+'.json', 'w')
        fileObject.write(jsObj)
        fileObject.close()

import requests
from lxml import etree

def read_more(i):
    with open(str(i)+".json", 'r') as f:
        temp = json.loads(f.read())
        contents = temp['blocks']
        for con in contents.get('items'):
            item = SpiderforbesItem()
            item["num"] = i
            item["title"] = con.get('title')
            item["url"] = con.get('url')
            item["description"] = con.get('description')
            item["author"] = con.get('author')['name']

            req = requests.get(item["url"])
            status_code = req.status_code
            # print(status_code)
            # 网页解码方式
            req.encoding = 'gb2312'
            # 获取网页源码 用html变量接收 text或content
            html = req.text
            # print(html)
            selector = etree.HTML(html)
            # 提取菜单栏url
            infros = selector.xpath('//*[@id="article-stream-0"]/div[2]/div[2]/div[3]/div[1]/p/text()')


            item["content"] = infros

            # timestamp

            item = ItemEncoder().encode(item)

            jsObj = json.dumps(item)

            fileObject = open(str(i)+ '_.json', 'w')
            fileObject.write(jsObj)
            fileObject.close()

            i += 1
