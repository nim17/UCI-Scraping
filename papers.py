# -*- coding: utf-8 -*-
import scrapy


class PapersSpider(scrapy.Spider):
    name = 'papers'
    allowed_domains = ['archive.ics.uci.edu/ml/datasets.php']
    start_urls = ['https://archive.ics.uci.edu/ml/datasets.php']

    def parse(self, response):
        papers = response.xpath('//table/tr/td/a/@href').extract()
        for paper in papers:
            absolute_url = 'https://archive.ics.uci.edu/ml/'+paper
            yield Request(absolute_url, callback=self.parse_book)
            
    def parse_book(self, response):
        para=response.xpath('//p[@class="normal"]/text()').extract()
        for line in para:
            if 'IEEE' in line:
                yield{'site' : line
                        }
