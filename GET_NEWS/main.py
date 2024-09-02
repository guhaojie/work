from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from RULE import rules

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())

    for rule in rules:
        process.crawl('common_spider', rule=rule)

#    process.crawl('common_spider', rule=rules[10])

    process.start()
    print("\n**************FINISHED**************")
