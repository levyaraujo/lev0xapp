from flask_jwt_extended import JWTManager
from config import settings

def init_auth(app):
    app.config['SECRET_KEY'] = settings.SECRET_KEY
    JWTManager(app)