import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import urllib.request

class ElectionSpiderSpider(CrawlSpider):
    name = 'election_spider'
    
    start_urls = ['https://dadosabertos.tse.jus.br/dataset/?groups=eleitorado']

    rules = (
        # Extract links matching 'eleitorado' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('eleitorado\-[0-9]+', )), callback='parse_item'),
    )

    def parse_item(self, response):
        file_url = response.css('.resource-url-analytics::attr(href)').get()
        self.logger.warning(file_url)
        file_name = file_url.split('/')[-1]
        with urllib.request.urlopen(file_url) as f:
            with open(f'E:\Repos\Brazilian-Election-Data-Analysis\ElectionData\downloads\{file_name}', 'wb') as out_file:
                out_file.write(f.read())