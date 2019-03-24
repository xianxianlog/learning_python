# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FoodmatePipeline(object):
    def process_item(self, item, spider):
        with open("food_nutrition.csv","a+",encoding="utf-8") as f:
            f.write(str(item))
            f.write("\n")
        return item
