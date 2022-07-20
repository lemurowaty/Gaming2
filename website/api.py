from flask_restful import Resource
from flask_login import login_required, current_user
from flask import request, jsonify
from . import db, Message, User, BasketItem
from datetime import datetime

class MessageApi(Resource):
    @login_required
    def post(self):
        data = request.json
        if data is None or "user_id_from" not in data or "user_id_to" not in data or "text" not in data:
            return jsonify(error="request body is invalid")

        user_from = User.query.get(data["user_id_from"])
        user_to = User.query.get(data["user_id_to"])
        if user_to and user_from:
            message = Message(user_id_from=user_from.id, user_id_to=user_to.id, text=data["text"], date_created=datetime.now())
            db.session.add(message)
            db.session.commit()
            return jsonify(data)

        return jsonify(error="Brak uzytkownika o podanym id")


class MessagesApi(Resource):
    @login_required
    def post(self):
        data = request.json
        if data is None or "last_update" not in data or "user_id" not in data:
            return jsonify(error="request body is invalid")
        last_update_date = datetime.strptime(data["last_update"], "%Y-%m-%dT%H:%M:%S")
        user_id = data["user_id"]

        msgs = []
        msgs += Message.query.filter(Message.user_id_from==current_user.id and Message.user_id_to==user_id)
        msgs += Message.query.filter(Message.user_id_from==user_id and Message.user_id_to==current_user.id)
        msgs.sort(key=lambda m: m.date_created)
        return jsonify([{"id" : m.id,
                         "user_id_from" : m.user_id_from,
                         "user_id_to" : m.user_id_to,
                         "text" : m.text,
                         "date_created" : m.date_created.strftime("%Y-%m-%dT%H:%M:%S") } for m in msgs if m.date_created >= last_update_date])


class BasketApi(Resource):
    @login_required
    def get(self):
        items = BasketItem.query.filter_by(user_id=current_user.id)
        return jsonify([item.game_id for item in items])

    @login_required
    def post(self):
        data = request.form
        if data is None or "gameID" not in data:
            return jsonify(error="request body is invalid")

        item = BasketItem(game_id=int(data["gameID"]), user_id=current_user.id)
        db.session.add(item)
        db.session.commit()
        db.session.refresh(item) #doda do obiektu nadany id
        return jsonify(status="success", game_id=item.game_id, item_id=item.id)
