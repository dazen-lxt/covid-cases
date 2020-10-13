# coding=utf-8

from marshmallow import Schema, fields
from sqlalchemy import Column, String

from .entity import Entity, Base


class Role(Entity, Base):
    __tablename__ = 'roles'

    name = Column(String)
    prefix = Column(String)

    def __init__(self, name, prefix, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.prefix = prefix

class RoleSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    prefix = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
    