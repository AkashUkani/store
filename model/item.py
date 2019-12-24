import sqlite3
from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer,db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name":self.name,"price":self.price,"store_id":self.store_id}

    @classmethod
    def create(cls):
        with sqlite3.connect('data.db') as connection:
            cursor = connection.cursor()
            query = 'create table items (id Integer primary key,name text,price float)'
            cursor.execute(query)

    @classmethod
    def drop(cls):
        with sqlite3.connect('data.db') as connection:
            cursor = connection.cursor()
            query = 'drop table if exists items'
            cursor.execute(query)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def getItem(cls,name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def getItems(cls):
        return [ item.json() for item in cls.query.all() ]

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
