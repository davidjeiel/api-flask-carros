from peewee import Model, IntegerField, CharField
from database.database import db_pw

class Carros(Model):
    id = IntegerField(primary_key=True)
    marca = CharField()
    modelo = CharField()
    ano = IntegerField()

    class Meta:
        database = db_pw  # This is the database connection