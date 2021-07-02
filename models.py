from datetime import datetime

from peewee import *


DATABASE = PostgresqlDatabase('whispering_oaks')

class Visitor(Model):
    name = CharField()
    number = IntegerField()
    email = CharField()
    message = TextField()
    created_at = DateTimeField(default=datetime.now)

    class Meta: 
        database = DATABASE
    
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Visitor], safe=True)
    print('PeeWee connected and tables created')
    DATABASE.close()
