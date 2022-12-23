from flask import Flask
from src.api.Controller import Routes
from .plugins import db, authentication
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    db.init_database()
    authentication.init_auth(app)
    Routes.init_app(app)
    CORS(app)

    return app