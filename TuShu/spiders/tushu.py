# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

from TuShu.items import TushuItem


class TushuSpider(scrapy.Spider):
    name = 'tushu'
    allowed_domains = ['m.wodeshucheng.com']
    # url = 'http://m.wodeshucheng.com/modules/article/wapreader.php?aid=4591&cid={}'
    start_urls = ['http://m.wodeshucheng.com/modules/article/wapreader.php?aid=4591&cid=1435275']
    """
    http://m.wodeshucheng.com/modules/article/wapreader.php?aid=4591&cid=1435275
    http://m.wodeshucheng.com/modules/article/wapreader.php?aid=4591&cid=1435276
    href="/modules/article/wapreader.php?aid=4591&cid=1435276"
    """

    def parse(self, response):
        item = TushuItem()
        item['title'] = "\n".join(response.xpath('//div[@id="nr_title"]/text()').extract())
        item['content'] = "\n".join(response.xpath('//div[@id="nr1"]/text()').extract())

        yield item
        print response.xpath('//a[@id="pb_next"]')
        if response.xpath('//a[@id="pb_next"]').extract_first():
            nex_url = 'http://m.wodeshucheng.com' + response.xpath('//a[@id="pt_next"]/@href').extract_first()
            print nex_url
            yield scrapy.Request(nex_url, callback=self.parse)
