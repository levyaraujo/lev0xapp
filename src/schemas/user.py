from marshmallow import Schema, fields


class UserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email()
    password = fields.Str(required=True)

class UserLogin(Schema):
    email = fields.Email()
    password = fields.String()