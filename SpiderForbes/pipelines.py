# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

from scrapy.exporters import JsonItemExporter




# class SpiderforbesPipeline(object):
#     def process_item(self, item, spider):
#         return item


class SpiderforbesPipeline(object):


    def open_spider(self, spider):
        # 这个函数是自己加的
        print('执行了pipelines.py的open_spider函数')

    def process_item(self, item, spider):
        # 这个函数是默认生成的 接收spiders扔过来的dict

        f = open('1' + '.json', 'w')
        json.dump(item, f)

        return item



