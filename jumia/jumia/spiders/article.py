from scrapy import Request , Spider
from ..items import ArticleItem
from jumia import items
class SpiderArticle(Spider):
    name="article"
    url= "https://www.jumia.com.tn/"
    def start_requests(self):
        yield Request(url=self.url , callback=self.parse_article)

    def parse_article(self,response):
        listeArticle=response.css('article.prd')
        for article in listeArticle:
            designations=article.css('a.core div.name::text').extract_first()
            picture=article.css('a.core img.img').attrib['data-src']
            price=article.css('a.core div.prc::text').extract_first()
            item=ArticleItem()
            item['designations']=designations
            item['picture']=picture
            item['price']=price

            yield item
