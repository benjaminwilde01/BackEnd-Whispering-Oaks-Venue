from datetime import datetime
import os
from peewee import *
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get(
        'postgres: // ukyriqaoykvzfy: ad8142353c61b8181a2be5fd1fd87afd5694be43b2557df525612310a32e87c2@ec2-52-0-67-144.compute-1.amazonaws.com: 5432/d8f9bkplq8552n'))

else:
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
