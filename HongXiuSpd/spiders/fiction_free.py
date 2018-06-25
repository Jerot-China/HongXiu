# -*- coding: utf-8 -*-
import scrapy
from ..items import HongxiuspdItem
from scrapy.http import Request
from lxml import etree


class FictionFreeSpider(scrapy.Spider):
    global headers
    global gender_id
    global base_url
    base_url = 'https://www.hongxiu.com'
    name = 'fiction_free'
    # 1为男生，2为女生
    gender_id = 1
    allowed_domains = ['www.hongxiu.com']
    start_urls = ['https://www.hongxiu.com/free/all?gender='+ str(gender_id)]
    headers = {"Accept":"application/json, text/javascript, */*; q=0.01",
               "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def parse(self, response):
        # 获取文章总数和每页数量，整除后再+1 得到文章总页面
        data_total = response.xpath("//div[@class='pagination']/@data-total").extract()[0]
        data_size = response.xpath("//div[@class='pagination']/@data-size").extract()[0]
        page = int(data_total)//int(data_size) + 1

        for i in range(1,2):
            # 拼接url
            next_url = 'https://www.hongxiu.com/free/all?gender='+ str(gender_id) + '&pageNum=' + str(i)
            print(next_url)
            yield Request(next_url, callback=self.get_fiction_url, headers=headers, dont_filter=True) 
        

    def get_message(self, response):
        global item
        # 获取性别,名称，种类，状态，字数，链接
        item = HongxiuspdItem()
        item['gender'] = gender_id
        item['name'] = response.xpath("//div[@class='book-info']/h1/em/text()").extract()
        item['category'] = response.xpath("//span[@class='tag']/i[3]/text()").extract()
        item['status'] = response.xpath("//span[@class='tag']/i[1]/text()").extract()
        item['words'] = response.xpath("//p[@class='total']/span[1]/text()").extract()
        #  接受meta
        item['url'] = response.meta['fiction_url']
        # 获取作者，简介，点击量，收藏量
        # 获取简介后转成字符串然后replace掉不需要的字符再转换成List并最终赋值给item['author']
        authors = response.xpath("//a[@class='writer default']/text()").extract()
        authors = ','.join(authors).replace(' ','').replace('著','')
        authors = authors.split(",")
        item['author'] = authors
        item['clicks'] = response.xpath("//p[@class='total']/span[3]/text()").extract()
        item['collections'] = response.xpath("//p[@class='total']/span[2]/text()").extract()
        item['introduce'] = response.xpath("//p[@class='intro']/text()").extract()
        # 获取目录
        directorys = response.xpath("//div[@class='volume']/ul/li/a/text()").extract()
        # 获取小说名
        name = item['name'][0]
        # 生成字典
        item['directory'] = {name:directorys}
    
        return item
        

    def get_fiction_url(self, response):
        urls = response.xpath("//div[@class='right-book-list']/ul/li//div[@class='book-info']/h3/a/@href").extract()

        for url in urls:
            fiction_url = base_url + url
            # 用meta传递url给回调函数
            yield Request(fiction_url, callback=self.get_message, headers=headers, meta={"fiction_url":fiction_url})
