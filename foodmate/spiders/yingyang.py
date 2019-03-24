# -*- coding: utf-8 -*-
import scrapy
from foodmate.items import FoodmateItem
import re
from lxml import html
import time
import copy


class YingyangSpider(scrapy.Spider):
    name = 'yingyang'
    allowed_domains = ['foodmate.net']
    start_urls = ["http://db.foodmate.net/yingyang"]

    def parse(self, response):
        food_kind_list=response.xpath("//div[@id='top']/a")[0:2]
        for food_kind in food_kind_list:
            item=FoodmateItem()
            item['kind']=food_kind.xpath("./text()").extract_first()
            food_kind_url = food_kind.xpath("./@href").extract_first()
            print(food_kind_url)
            yield scrapy.Request(self.start_urls[0]+"/"+food_kind_url,
                                 callback=self.parse_food,
                                 meta={'item':item})
            time.sleep(2)


    def parse_food(self,response):
        item=response.meta['item']
        food_list=response.xpath("//div[@id='dibu']/li")
        for food in food_list:
            # 这里要用deepcopy新建一个对象，
            # 因为上面的item是分类时创建的item，小分类中用的是大分类创建的item
            # 小分类赋值时，后面添加的item字段会把前面的item字段覆盖
            item=copy.deepcopy(item)
            item['food_name']=food.xpath("./a/text()").extract_first()
            detail_url=food.xpath("./a/@href").extract_first()
            print(detail_url)
            yield scrapy.Request(self.start_urls[0]+"/"+detail_url,
                                 callback=self.parse_detail,
                                 meta={'item':item}
                                 )


    def parse_detail(self,response):
        item=response.meta['item']
        detail_list=response.xpath("//div[@id='rightlist']//div[@class='list']").extract()
        nutrition={}
        for detail in detail_list:
            #print(detail)
            ret=re.match(r"<div class=\"list\"><div class=\"list_m\">(.*)</div>(.*)</div>",detail)
            if(ret):
                nutrition[ret.group(1)]=ret.group(2)
        item['nutrition']=nutrition
        yield item

