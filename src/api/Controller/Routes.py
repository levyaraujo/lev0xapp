from ..Controller.User import *
from ..Controller.Chat import *

bp = Blueprint('api', __name__)
api = Api(bp)

def init_app(app):
    api.add_resource(Home, "/")
    api.add_resource(UserRegister, "/user")
    api.add_resource(UserActions, "/user/<id>")
    api.add_resource(Login, "/login")
    api.add_resource(Chat, '/chat')
    
    app.register_blueprint(bp)