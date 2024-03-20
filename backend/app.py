from flask import Flask
from flask_cors import CORS,cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
import os

app = Flask(__name__)

CORS(app, resources={r"/api": {"origins": "*"}})

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'beautylensdb.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

login = LoginManager(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)

import routes, models

with app.app_context():
    db.create_all()