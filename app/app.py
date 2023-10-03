
from flask import Flask, make_response
from flask_migrate import Migrate
from flask_rest import Api, Resource, Namespace, fields

from models import db, Hero, Power, HeroPower
from exceptions import ObjectNotFoundException

ns = Namespace("/")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
