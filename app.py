from flask import Flask
from random import randint
from models import *
from os import path


app = Flask(__name__)


# Генерация новой комнаты
# http://127.0.0.1:5000/new_room/admin=ahramcov/money=2000/max_count_players=5
@app.route('/new_room/admin=<admin_name>/money=<money>/max_count_players=<count>', methods = ['GET'])
def generate_room(admin_name, money, count):
    while True:
        number_room = randint(100000,999999)
        if not path.exists(f'rooms\{number_room}.txt'):
            break
    room(str(number_room), admin_name, money, count)
    return room.load_from_json(str(number_room))


# Получение инфорамции об игровой комнате
# http://127.0.0.1:5000/room=227281
@app.route('/room=<room_id>', methods = ['GET'])
def get_about_room(room_id):
    return room.load_from_json(room_id)


# Получение информации о пользователе в комнате
# http://127.0.0.1:5000/room=227281/user=konorev
@app.route('/room=<room_id>/user=<user>', methods = ['GET'])
def get_about_user(room_id, user):
    return room.get_about_user(room_id, user)


# Добавить пользователя в комнату
# http://127.0.0.1:5000/room=227281/add_user=konorev
@app.route('/room=<room_id>/add_user=<user>', methods = ['GET'])
def add_user(room_id, user):
    return room.add_user(room_id, user)


# Удалить пользователя из комнаты
# http://127.0.0.1:5000/room=227281/del_user=konorev
@app.route('/room=<room_id>/del_user=<user>', methods = ['GET'])
def del_user(room_id, user):
    return room.del_user(room_id, user)


# Удалить комнату
# http://127.0.0.1:5000/del_room=227281
@app.route('/del_room=<room_id>', methods = ['GET'])
def del_room(room_id):
    return room.del_room(room_id)


# Добавить (отнять) пользователю денег
# http://127.0.0.1:5000/room=227281/user=konorev/add_money=1000
@app.route('/room=<room_id>/user=<user>/add_money=<money>', methods = ['GET'])
def add_money(room_id, user, money):
    return room.add_money(room_id, user, money)


if __name__ == '__main__':
    app.run(debug=True)