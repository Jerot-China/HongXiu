# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import re


class HongxiuspdPipeline(object):


    def __init__(self):
        self.conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="123456",
            db="hongxiu",
            charset="utf8")

    def process_item(self, item, spider):

        # 存储数据
        # for j in range(0,len(item['name'])):
        for j in range(0, 1):
            name = item['name'][j]
            url = item['url']
            category = item['category'][j]
            words = item['words'][j]
            status = item['status'][j]
            gender = item['gender']
            collections = item['collections'][j]
            clicks = item['clicks'][j]
            author = item['author'][j]
            introduce = item['introduce'][j]
            # 执行Insert语句
            sql = "insert into fiction(name,category,status,gender,words,collections,clicks,author,introduce,url) VALUES ('"+ name +"','"+ category +"','"+ status +"','"+ str(gender) +"','"+ words +"',\
            '"+ collections +"','"+ clicks +"','"+ author+"','"+ introduce +"','"+ url +"')"
            # 提交并执行sql语句
            self.conn.query(sql)
            self.conn.commit()

            # 查询小说在数据库中的id
            id_sql = "select id from fiction where name='{}'".format(name)
            # 创建游标用来进行查询
            cursor1 = self.conn.cursor()
            cursor1.execute(id_sql)
            # 获取fiction_id
            fiction_id = cursor1.fetchone()
            # 使用replace方法来获取数字
            # fiction_id = str(fiction_id).replace('(','').replace(')','').replace(',','')
            # 使用正则的方式来获取字符串中的数字
            reg = r"\d+\.?\d*"
            fiction_id = re.search(reg,str(fiction_id)).group(0)

            # 遍历整个item['directory']中的值，拿到每一章的名字
            for directory_name in item['directory'][name]:
                # 拼接插入sql
                directory_sql = "insert into fiction_directory(fiction_name,fiction_directory_name,fiction_id) \
                VALUES ('"+ str(name) +"','"+ str(directory_name) +"','"+ str(fiction_id) +"')"
                self.conn.query(directory_sql)
                self.conn.commit()                
            
        return item

    def close_spider(self, spider):
        self.conn.close()
