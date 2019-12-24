
from model.item import ItemModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask import request

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("price",
        type=float,
        required=True,
        help="This arg is required")
    parser.add_argument("store_id",
        type=int,
        required=True,
        help="This arg is required")

    @jwt_required()
    def get(self,name):
        item = ItemModel.getItem(name)
        return (item.json(),200) if item else ({"message":"Item not found"},400)

    def post(self,name):
        if ItemModel.getItem(name):
            return {"message":"item already exists"},400
        data = Item.parser.parse_args()
        item = ItemModel(name,data['price'],data['store_id'])
        item.save_to_db()
        return item.json(),201

    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.getItem(name)
        if item is None:
            item = ItemModel(name,data['price'],data['store_id'])
        else:
            item.price = data['price']
            item.store_id = data['store_id']
        item.save_to_db()
        return item.json()

    def delete(self,name):
        item = ItemModel.getItem(name)
        if item:
            item.delete_from_db()
        return {'message':'item successfully Deleted'},200

class Items(Resource):

    def get(self):
        return { 'items' : ItemModel.getItems() }
