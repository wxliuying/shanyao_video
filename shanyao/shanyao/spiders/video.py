import scrapy
import lxml.etree
from scrapy_redis.spiders import RedisSpider


class VideoSpider(scrapy.Spider):
    name = 'video'
    allowed_domains = ['ixigua.com']
    start_urls = ['https://www.ixigua.com/home/61676875255/?list_entrance=search']
    # keys = "shanyao"

    # def make_requests_from_url(self, url):
    #     return scrapy.Request(url,dont_filter=True)

    def parse(self, response):
        # print(len(response.body))
        data = []
        node_list = response.xpath('//*[@id="App"]/div/main/div/div[2]/div[1]/div[2]/div[1]/div')
        print(node_list)
        for node in node_list:
            item = {}
            link = response.urljoin(node.xpath('./div[2]/div/a/@href').extract_first())
            time = node.xpath('./div[2]/div/div/span/text()').extract_first()
            # print(link,time)
            # print(len(node_list))
            item['link'] = link
            item['time'] = time
            # data.append(item)
            yield item

