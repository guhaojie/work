# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import jieba
from jieba.analyse import *


jieba.setLogLevel(jieba.logging.INFO)

class GenNewsKWPipeline:
    def process_item(self, item, spider):
        data = ' '.join(item['nsTITLE']) + ' '.join(item['nsCONTENT'])
        for keyword in textrank(data, topK=5, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')):
            item['nsKEYWORDS'].append(f"#{keyword} ")
        return item


class SaveNewsPipeline:
    def process_item(self, item, spider):
        with open(f"/Users/haojiegu/Library/Application Support/DEVONthink 3/Inbox/{item['nsTITLE']}.md", "w") as f:
            print(item['nsTITLE'])
            f.write("# " + item['nsTITLE'])
            f.write("\n")
            f.write(item['nsURL'])
            f.write("\n\n\n")
            f.writelines(item['nsCONTENT'])
            f.write("\n\n")
            f.writelines(item['nsKEYWORDS'])
        return item
