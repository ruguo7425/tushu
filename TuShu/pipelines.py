# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import re匹配


class TushuPipeline(object):
    def open_spider(self, spider):
        self.f = open('chun.txt', 'w')

    def process_item(self, item, spider):
        content = (json.dumps(dict(item), ensure_ascii=False) + ",\n").encode(('utf-8'))
        self.f.write(content)

    def close_spider(self, spider):
        self.f.close()
