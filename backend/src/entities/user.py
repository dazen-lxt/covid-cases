# coding=utf-8

from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .entity import Entity, Base


class User(Entity, Base):
    __tablename__ = 'users'

    name = Column(String)
    lastname = Column(String)
    code = Column(String)
    phone = Column(String)
    address = Column(String)
    email = Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role")

    def __init__(self, name, lastname, code, phone, address, email, role_id, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.lastname = lastname
        self.code = code
        self.phone = phone
        self.address = address
        self.email = email
        self.role_id = role_id

class UserSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    lastname = fields.Str()
    code = fields.Str()
    phone = fields.Str()
    address = fields.Str()
    email = fields.Str()
    role_id = fields.Integer()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
    