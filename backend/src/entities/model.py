# coding=utf-8

from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .entity import Entity, Base


class Model(Entity, Base):
    __tablename__ = 'models'

    name = Column(String)
    description = Column(String)
    file_name = Column(String)
    file_path = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")

    def __init__(self, name, description, file_name, file_path, user_id, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.description = description
        self.file_name = file_name
        self.file_path = file_path
        self.user_id = user_id

class ModelSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    description = fields.Str()
    file_name = fields.Str()
    file_path = fields.Str()
    user_id = fields.Integer()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
    