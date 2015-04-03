# -*- coding:utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from image_downloader_mimi.items import ImageDownloaderMimiItem
import os

class ImageDownloaderSpider(CrawlSpider):
    name = "image_mimi"
    allowed_domains = ["www.skymimi.com"]
    start_urls = ["http://www.skymimi.com/forumdisplay.php?fid=59&page=%s" % x for x in range(3,5)]
    rules = [Rule(LinkExtractor(allow=['viewthread\.php\?tid=\d+']), 'parse_item')]

    def parse_item(self, response):
        self.log('page: %s' % response.url)
        #name = response.xpath('//span[@class="bold"]/text()').extract()[1].encode('utf-8')
        images = response.xpath('//img[@onmouseover]/@src').extract()
        items = []
        for image in images:
            item = ImageDownloaderMimiItem()
            #item['name'] = [name]
            item['image_urls'] = [image]
            items.append(item)
            #if os.path.isdir(name) == False:
            #   dir = 'download/full/' + name
            #   os.mkdir(dir)
        return items