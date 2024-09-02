from scrapy import signals
from scrapy.exceptions import NotConfigured
from tqdm import tqdm

class ProgressBar:
    def __init__(self, crawler):
        self.crawler = crawler
        self.bars = {}
        self.total = crawler.stats.get_value('item_scraped_count', 0)

    @classmethod
    def from_crawler(cls, crawler):
        ext = cls(crawler)
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
        return ext

    def spider_opened(self, spider):
        self.bars[spider.file_name_prefix_rule] = tqdm(total=self.total,
                                                       desc=f"{spider.file_name_prefix_rule}\t",
                                                       unit="item",
                                                       position=0,
                                                       leave=True)

    def item_scraped(self, item, spider):
        self.bars[spider.file_name_prefix_rule].update(1)

    def spider_closed(self, spider):
        self.bars[spider.file_name_prefix_rule].close()
