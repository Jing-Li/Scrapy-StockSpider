# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import csv
import os
class StockPipeline(object):
    
    def __init__(self):
        if os.path.exists('stock.csv'):
            os.remove('stock.csv')
        
    
    def process_item(self, item, spider):
        ofile = open('stock.csv', 'a')
        writer = csv.writer(ofile, dialect='excel')
        writer.writerow([item['stockNameID'][0].encode('utf-8'),
                        item['price'][0].encode('utf-8'),
                        item['time'][0].encode('utf-8')])
        ofile.close()
        return item
