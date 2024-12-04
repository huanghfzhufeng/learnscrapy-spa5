# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LearnscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class SPA5Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 书名
    author = scrapy.Field()  # 作者
    price = scrapy.Field()  # 价格
    time = scrapy.Field()  # 出版时间
    press = scrapy.Field()  # 出版社
    page = scrapy.Field()  # 页数
    isbm = scrapy.Field()  # ISBN
    comments = scrapy.Field()  # 评论信息，列表格式，每个元素是字典，包含评论内容等
