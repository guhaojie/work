from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from RULE import rules


def start_get_news():
    process = CrawlerProcess(get_project_settings())

    for rule in rules:
        process.crawl('common_spider', rule=rule)

    process.start()
    print("\n**************FINISHED**************")


if __name__ == '__main__':
    start_get_news()
