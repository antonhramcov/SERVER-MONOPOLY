## Сервер для игры в монополию ##
### Функционал: ###
1. Создание/удаление отдельных игровых комнат.
2. Добавление/удаление пользователей в комнате.
3. Изменение игрового баланса пользователей.
4. Запрос информации о комнате.
5. Запрос информации о конкретном пользователе.

### Как запустить сервер: ###
1. Установить язык программирования Python.
Для работы с Flask вам понадобится Python версии 3.6 или выше. Если у вас еще не установлен Python, вы можете скачать его с [официального сайта](python.org) Python.
2. Flask можно установить с помощью инструмента управления пакетами Python, pip. Откройте терминал или командную строку и введите команду: ``` pip install Flask ```.
3. Запустить приложение ``` app.py ```  -  ``` python app.py ```

### Запросы к серверу: ###
* **Создание игровой комнаты**
```http://127.0.0.1:5000/new_room/admin=ahramcov/money=2000/max_count_players=5``` - Создать новую комнату, определить администратора с ником ``` ahramcov ```, стартовым количеством денег для каждого пользователя ``` 2000 ```, максимальным количеством игроков в комнате ``` 5``` (включая администратора).
Ответ сервера:
```json
{
  "admin":{
    "ahramcov": "2000"
  },  
  "date": "2024-02-12 14:43:16.248170",  
  "max_count_players": "5",  
  "number": "227281",  
  "start_money": "2000",  
  "status": true,  
  "users": {
  }
}
```
* **Получение информации о комнате**
```http://127.0.0.1:5000/room=227281``` - Получить информацию об игровой комнате с id ```227281```. Ответ сервера:
```json
{
  "admin": {
    "ahramcov": "2000"
  },
  "date": "2024-02-12 13:38:20.066872",
  "max_count_players": "5",
  "number": "227281",
  "start_money": "2000",
  "status": true,
  "users": {
    "konorev": "3000"
  }
}
```
* **Получение информации о пользователе в комнате**
```http://127.0.0.1:5000/room=227281/user=konorev``` - Получить информацию о пользователе ```konorev``` из игровой комнаты ```227281```. Ответ сервера:
```json
{"konorev": "3000"}
```
* **Добавить пользователя в комнату**
```http://127.0.0.1:5000/room=227281/add_user=markin``` - Добавить пользователя ```konorev``` в комнату ```227281```. Ответ сервера:
```json
user markin added in room 227281
```
* **Удалить пользователя из комнаты**
```http://127.0.0.1:5000/room=227281/del_user=markin``` - Удалить пользователя ```markin``` из комнаты ```227281```. Ответ сервера:
```json
user markin deleted from room 227281
```
* **Удалить комнату**
```http://127.0.0.1:5000/del_room=227281``` - Удалить комнату ```227281```. **Ответ сервера:**
```json
room 227281 was deleted
```
* **Добавить пользователю денег**
``` http://127.0.0.1:5000/room=227281/user=konorev/add_money=1000``` - Добавить ```1000``` пользователю ```konorev``` в комнате ```227281```. Ответ сервера:
```json
user konorev get 1000 money in room 227281
```
* **Отнять у пользователя деньги**
``` http://127.0.0.1:5000/room=227281/user=konorev/add_money=-2000``` - Отнять ```2000``` у пользователя ```konorev``` в комнате ```227281```. Ответ сервера:
```json
user konorev get -2000 money in room 227281
```
### Ошибки сервера: ###
* **Комната с ```id_room``` не найдена**
```json
error: room with number {id_room} not found :/
```
Создайте новую комнату.
* **Достигнуто максимальное количество игроков в комнате ```id_room```**
```json
Maximum number of players in a room {id_room} :-(
```
Для данной комнаты достигнуто максимальное количество пользователей.
* **Пользователь ```name```в комнате ```id_room```не найден**
```json
error: user {name} not found in room {id_room} :((
```
Добавьте данного пользователя в комнату.

### Авторы проекта: ###
1. [Антон Храмцов](https://t.me/ahramcov2022)
2. [Алексей Конорев](https://t.me/Docitin)