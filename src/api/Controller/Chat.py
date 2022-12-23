from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from config import settings

class Chat(Resource):
    @jwt_required()
    def get(self):
        logged_user = get_jwt_identity()
        return {"welcome": logged_user}, 200
