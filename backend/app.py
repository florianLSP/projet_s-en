from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./habits.db"

    db.init_app(app)

    from routes import register_routes

    register_routes(app, db)

    Migrate(app, db)

    CORS(app)

    return app
