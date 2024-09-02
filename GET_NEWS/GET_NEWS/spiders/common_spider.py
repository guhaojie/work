import scrapy
from scrapy.http import Response
from .. import items


class commonSpider(scrapy.Spider):
    name = "common_spider"

    def __init__(self, rule):
        self.__dict__.update(rule)
        super(commonSpider, self).__init__()

    def _trans(self, r, d):
        if hasattr(self, r):
            return self.__dict__[r]
        else:
            return d

    def parse(self, response):
        news_links = (response
                      .xpath(self._trans('news_url_rule', '//html'))
                      .re(self._trans('news_url_reg_rule', r'(.*)?')))
        for news_link in news_links:
            if news_link:
                yield scrapy.Request(self.news_url_prefix_rule + news_link,
                                     callback=self.parse_detail)

        next_page = response.xpath(self.news_next_page_url_rule).get()
        if next_page:
            next_page = self.news_next_page_url_prefix_rule + next_page
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_detail(self, response):
        try:
            _ns_title = response.xpath(self.news_title_rule).get().replace("\n", "").strip()
        except AttributeError:
            _ns_title = "None"

        ns_title = (self.file_name_prefix_rule + "_" + _ns_title)
        ns_url = response.url
        ns_content = response.xpath(self.news_content_rule).getall()
        ns_content = [_.strip() + "\n\n" for _ in ns_content]
        ns_keywords = []

        yield items.GetNewsItem(
            nsTITLE=ns_title,
            nsURL=ns_url,
            nsCONTENT=ns_content,
            nsKEYWORDS=ns_keywords
        )
