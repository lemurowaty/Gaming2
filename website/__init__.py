from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_restful import Api
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', "sqlite:///database.db").replace("postgres", "postgresql")
app.config["SECRET_KEY"] = "1234567"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from .views import *

from .models import User, Message, BasketItem
migrate = Migrate(app=app, db=db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

from .api import MessageApi, MessagesApi, BasketApi
api = Api(app)
api.add_resource(MessageApi, '/api/message')
api.add_resource(MessagesApi, '/api/messages')
api.add_resource(BasketApi, '/api/basket')

