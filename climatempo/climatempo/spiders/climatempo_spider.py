# -*- coding: utf-8 -*-
import scrapy
from . import util

class ExampleSpider(scrapy.Spider):
    name = 'climatologia'
    allowed_domains = ['climatempo.com.br']
    # as required by the test
    start_urls = util.gen_start_urls()

    def parse(self, response):
        if response.url.split('/')[-1] != 'ops':
            table = response.css("tbody td::text").extract()
            yield {response.url.split('/')[-1]: table}
