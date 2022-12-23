from flask_restful import Resource, Api, request
from flask import Blueprint
from config import settings
import json
from ...schemas.user import UserSchema, UserLogin
from ...models.user import User
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required

class Home(Resource):
    def get(self):
        return {"Hello": settings.MESSAGE}, 200

class UserRegister(Resource):
    def post(self):
        data = json.loads(request.data)
        try:
            result = UserSchema().load(data)
            if result:
                data['password'] = generate_password_hash(data['password'])
                user = User(**data)
                user.save()
            return {"success": "User successfully created"}, 201
        except ValidationError as error:
            return error.messages, 403
        except Exception as error:
            print(error)


class UserActions(Resource):
    @jwt_required()
    def delete(self, id: int):
        try:
            print(id)
            User.delete(id=int(id))
            return {"deleted": "User successfully deleted"}, 200

        except Exception as error:
            return {"error": "Ocurred an unexpected error"}, 500

class Login(Resource):
    def post(self):
        data = json.loads(request.data)
        try:
            validate = UserLogin().load(data)
            if validate:
                user = User.exists(data['email'])
            if user and check_password_hash(user['password'], data['password']):
                token = create_access_token(identity=user['username'])
                return {"token": token}
            return {"error": "Your email or password are wrong."}, 403
        
        except ValidationError as error:
            return error.messages, 400