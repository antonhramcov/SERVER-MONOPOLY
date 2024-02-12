from datetime import *
from json import *
from os import path

class room:
    def __init__(self, number:str, admin_name:str, money:str, max_count_players:str):
        self.number = number
        self.max_count_players = max_count_players
        self.start_money = money
        self.date = str(datetime.now())
        self.admin = {admin_name:money}
        self.users = {}
        self.status = True
        data = {
            'number': self.number,
            'max_count_players': self.max_count_players,
            'start_money': self.start_money,
            'date': self.date,
            'admin': self.admin,
            'users': self.users,
            'status': self.status
        }
        with open(f'rooms\{number}.txt', 'w', encoding='utf-8') as f:
            f.write(dumps(data))



    def load_from_json(id_room:str):
        if path.exists(f'rooms\{id_room}.txt'):
            with open(f'rooms\{id_room}.txt', 'r', encoding='utf-8') as f:
                from_json = loads(f.read())
            return from_json
        else:
            return f'error: room with number {id_room} not found :/'


    def save_to_json(id_room:str, room):
        data = {
            'number':room['number'],
            'max_count_players':room['max_count_players'],
            'start_money':room['start_money'],
            'date':room['date'],
            'admin':room['admin'],
            'users':room['users'],
            'status':room['status']
        }
        with open(f'rooms\{id_room}.txt', 'w', encoding='utf-8') as f:
            f.write(dumps(data))

    def add_user(id_room:str, name:str):
        if path.exists(f'rooms\{id_room}.txt'):
            from_json = room.load_from_json(id_room)
            if int(from_json['max_count_players'])>len(from_json['users'])+2:
                from_json['users'][name] = from_json['start_money']
                room.save_to_json(id_room, from_json)
                return f'user {name} added in room {id_room}'
            else:
                return f'error: Maximum number of players in a room {id_room} :-('
        else:
            return f'error: room with number {id_room} not found :/'


    def del_user(id_room:str, name:str):
        if path.exists(f'rooms\{id_room}.txt'):
            from_json = room.load_from_json(id_room)
            if name in from_json['users']:
                del from_json['users'][name]
                room.save_to_json(id_room, from_json)
                return f'user {name} deleted from room {id_room}'
            else:
                return f'error: user {name} not found in room {id_room} :(('
        else:
            return f'error: room with number {id_room} not found :/'


    def add_money(id_room:str, name:str, money:str):
        if path.exists(f'rooms\{id_room}.txt'):
            from_json = room.load_from_json(id_room)
            if name in from_json['users']:
                from_json['users'][name] = str(int(from_json['users'][name]) + int(money))
                room.save_to_json(id_room, from_json)
                return f'user {name} get {money} money in room {id_room}'
            elif name in from_json['admin']:
                from_json['admin'][name] = str(int(from_json['admin'][name]) + int(money))
                room.save_to_json(id_room, from_json)
                return f'user {name} get {money} money in room {id_room}'
            else:
                return f'error: user {name} not found in room {id_room} :(('
        else:
            return f'error: room with number {id_room} not found :/'


    def get_about_user(id_room:str, name:str):
        if path.exists(f'rooms\{id_room}.txt'):
            from_json = room.load_from_json(id_room)
            if name in from_json['users']:
                return dumps({name:from_json['users'][name]})
            elif name in from_json['admin']:
                return dumps({name: from_json['admin'][name]})
            else:
                return f'error: user {name} not found in room {id_room} :(('
        else:
            return f'error: room with number {id_room} not found :/'


    def del_room(id_room:str):
        if path.exists(f'rooms\{id_room}.txt'):
            from_json = room.load_from_json(id_room)
            from_json['status'] = False
            return f'room {id_room} was deleted'
        else:
            return f'error: room with number {id_room} not found :/'