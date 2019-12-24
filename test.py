
import sqlite3
from model.userDAO import UserDAO
from model.user import UserModel
from model.item import ItemModel
from resource.item import Item
#connection = sqlite3.connect('user.db')
dao = UserDAO('data.db')
#cursor = connection.cursor()

#cursor.execute('drop table if exists users')
#dao.drop()

#cursor.execute('create table users (id Integer primary key,username text,password text)')
#dao.create()

#u1 = UserModel('Akash','1234')
#u2 = UserModel('Vivek','910')
#u3 = UserModel('Meet','5678')
#cursor.executemany('insert into users values (Null,?,?)',[('Akash','1234'),('Meet','5678')])
#dao.insertUser(u1)
#dao.update(u2)
#dao.insertUser(u3)


print("$$$$$$$$$$")
for row in dao.getAllUsers():
    print(row)
print("$$$$$$$$$")

#print(dao.getUserByuserid(2))
#print(dao.getUserByusername('Akash'))
#print(dao.delete(2))

#for row in dao.getAllUsers():
#    print(row)

#print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#ItemModel.drop()
#ItemModel.create()
#i1 = ("Chair",15.99)
#i2 = ("Table",17.99)

#ItemModel.insertItem(i1)
#ItemModel.insertItem(i2)
#print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

for row in ItemModel.getItems():
    print(row)

#connection.commit()
#connection.close()
