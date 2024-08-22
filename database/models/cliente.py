from peewee import Model, CharField, DateField
from database.database import db
import datetime

class Cliente(Model):
    nome = CharField()
    email = CharField()
    data_registro = DateField(default=datetime.datetime.now)

    class Meta:
        database= db