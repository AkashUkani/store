
from flask import Flask,request
from flask_jwt import JWT
from flask_restful import Api
from security import authenticate, identity
from resource.item import Item,Items
from resource.store import Store, StoreList
from resource.user import UserRegister
from datetime import timedelta
from db import db
import os

app = Flask(__name__)
app.secret_key = "you can never guess"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_AUTH_URL_RULE'] = '/login'
api = Api(app)



jwt = JWT(app,authenticate,identity)
#app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=180)
#items=[]




api.add_resource(Item,"/item/<string:name>")
api.add_resource(Items,"/items")
api.add_resource(UserRegister,"/user")
api.add_resource(Store,"/store/<string:name>")
api.add_resource(StoreList,"/stores")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000,debug=True)
