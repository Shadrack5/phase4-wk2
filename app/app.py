
from flask import Flask, make_response
from flask_migrate import Migrate
from flask_rest import Api, Resource, Namespace, fields

from models import db, Hero, Power, HeroPower
from exceptions import ObjectNotFoundException

ns = Namespace("/")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)
api.add_namespace(ns)

power_model = api.model(
    "Power", {"id": fields.Integer, "name": fields.String, "description": fields.String}
)

power_input_model = api.model("Power", {"description": fields.String})

hero_model = api.model(
    "Hero",
    {"id": fields.Integer, "name": fields.String, "super_name": fields.String},
)

single_hero_model = api.model(
    "Hero",
    {
        "id": fields.Integer,
        "name": fields.String,
        "super_name": fields.String,
        "powers": fields.Nested(power_model),
    },
)

hero_power_model = api.model(
    "HeroPower",
    {
        "id": fields.Integer,
        "strength": fields.String,
        "power_id": fields.Integer,
        "hero_id": fields.Integer,
    },
)

hero_power_input_model = api.model(
    "HeroPower",
    {
        "strength": fields.String,
        "power_id": fields.Integer,
        "hero_id": fields.Integer,
    },
)

