# coding=utf-8  
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from stock.items import StockItem
class StockSpider(BaseSpider):
    name = "stockspider"
    start_urls = [
                  "http://hk.finance.yahoo.com/q?s=3988.HK",
                  "http://hk.finance.yahoo.com/q?s=600030.SS",
                  ]
    
    def parse(self, response):
        response = response.replace(body = response.body.decode('utf-8'))
        hxs = HtmlXPathSelector(response)
        item = StockItem()
        all = hxs.select('//div[@class="yfi_rt_quote_summary"]')
        item['stockNameID'] = all.select('//div[@class="title"]/h2/text()').extract()
        item['price'] = all.select('//span[@class="time_rtq_ticker"]/span/text()').extract()
        item['time'] = all.select('//span[@class="time_rtq"]/span/span/text()').extract()
        return item
