import scrapy
from scrapy import Request

from learnscrapy.items import SPA5Item


class SPA5Spider(scrapy.Spider):
    name = "spa5"
    offset = 0
    limit = 18
    url = f'https://spa5.scrape.center/api/book/?limit={limit}&offset=%s'

    def start_requests(self):
        urls = [self.url % self.offset]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        result = response.json()
        print(response.url)
        for a in result['results']:
            item = SPA5Item()
            item['title'] = a['name']
            item['author'] = '/'.join(a['authors'] or [])
            # 请求书籍详情页
            yield Request(url=f'https://spa5.scrape.center/api/book/{a["id"]}/', callback=self.parse2,
                          meta={'item': item})
        # 判断是否还有更多数据
        if int(result['count']) > self.offset:
            self.offset += self.limit
            yield Request(url=self.url % self.offset, callback=self.parse)

    def parse2(self, response):
        item = response.meta['item']
        result = response.json()
        
        item['price'] = result['price'] or 0
        item['time'] = result['published_at']
        item['press'] = result['publisher']
        item['page'] = result['page_number']
        item['isbm'] = result['isbn']

        # 提取评论信息
        comments = result.get('comments', [])
        item['comments'] = [{'id': comment['id'], 'content': comment['content']} for comment in comments]
        # 输出数据  
        print(item)
        yield item
