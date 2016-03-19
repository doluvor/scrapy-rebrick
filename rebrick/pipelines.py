# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class RebrickPipeline(object):

    insert_sql = """insert into rebrick_sets (%s) values ( %s )"""

    def __init__(self):
        dbargs = settings.get('DB_CONNECT')
        db_server = settings.get('DB_SERVER')
        dbpool = adbapi.ConnectionPool(db_server, **dbargs)
        self.dbpool = dbpool
        

    def __del__(self):
        self.dbpool.close()

    def process_item(self, item, spider):
        self.insert_data(item, self.insert_sql)
        print('-- Inserted item')
        return item

    def insert_data(self, item, insert):
        keys = item.fields.keys()
        fields = u','.join(keys)
        qm = u','.join([u'%s'] * len(keys))
        sql = insert % (fields, qm)
        data = [item[k] for k in keys]
        print(sql)
        print(data)
        return self.dbpool.runOperation(sql, data)

    def _handle_error(self, failure, item, spider):
        log.err(failure)
