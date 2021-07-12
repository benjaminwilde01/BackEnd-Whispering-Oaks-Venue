from datetime import date, datetime
import os
from peewee import *
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ:
    DATABASE = PostgresqlDatabase('dbc96ieitkn0a', user='yogyyqwrfeqeyd', password='1faaea5fc4d57f14421b9bf56a1291051891731f715bb62cd7c27605a8e7dc72',
                                  host='ec2-52-5-1-20.compute-1.amazonaws.com', port=5432)

else:
    DATABASE = PostgresqlDatabase('whispering_oaks')


class Visitor(Model):
    name = CharField()
    number = IntegerField()
    email = CharField()
    date = DateField()
    message = TextField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Visitor], safe=True)
    print('PeeWee connected and tables created')
    DATABASE.close()
