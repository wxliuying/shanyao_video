# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter


class ShanyaoPipeline:
    def __init__(self):
        self.file = open('E:/python笔记/text/shanyao/1.json','w')
    def process_item(self, item, spider):
        data = json.dumps(item,ensure_ascii=False) + ' \n'
        self.file.write(data)

        return item
    def __del__(self):
        self.file.close()
