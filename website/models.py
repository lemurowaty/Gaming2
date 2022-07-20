from flask_login import UserMixin
from . import db
from sqlalchemy import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), default="")
    password = db.Column(db.String(150))
    postcode = db.Column(db.String(6))


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id_from = db.Column(db.Integer, db.ForeignKey("user.id"))
    user_id_to = db.Column(db.Integer, db.ForeignKey("user.id"))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    text = db.Column(db.String(300))


class BasketItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
