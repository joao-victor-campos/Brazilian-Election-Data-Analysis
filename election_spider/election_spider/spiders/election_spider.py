import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import urllib.request
from zipfile import ZipFile

def extractor (file_name):
    for i in file_name:
        with ZipFile('E:\\Repos\\Brazilian-Election-Data-Analysis\\Election_Data\\' + i) as myZip:
            csv = [file for file in myZip.namelist() if ('.csv' or '.txt') in file] 
            myZip.extractall(members=csv, path='E:\Repos\Brazilian-Election-Data-Analysis\Election_Data')

class ElectionSpiderSpider(CrawlSpider):
    name = 'election_spider'
    
    start_urls = ['https://dadosabertos.tse.jus.br/dataset/?groups=eleitorado']

    rules = (
        # Extract links matching 'eleitorado' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('eleitorado\-[0-9]+', )), callback='parse_item'),
    )

    def parse_item(self, response):
        list = []
        file_url = response.css('.resource-url-analytics::attr(href)').get()
        self.logger.info(file_url)
        file_name = file_url.split('/')[-1]
        list = [file_name]
        with urllib.request.urlopen(file_url) as f:
            with open(f'E:\Repos\Brazilian-Election-Data-Analysis\Election_Data\{file_name}', 'wb') as out_file:
                out_file.write(f.read())
        extractor(list)