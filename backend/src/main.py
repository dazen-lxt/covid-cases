# coding=utf-8

from flask_cors import CORS
from flask import Flask, jsonify, request
import logging
from .entities.entity import Session, engine, Base
from .entities.role import Role, RoleSchema
from .entities.user import User, UserSchema
from .entities.model import Model, ModelSchema

# creating the Flask application
app = Flask(__name__)
CORS(app)
Base.metadata.create_all(engine)

@app.route('/roles')
def get_role():
    # fetching from the database
    session = Session()
    role_objects = session.query(Role).all()

    # transforming into JSON-serializable objects
    schema = RoleSchema(many=True)
    roles = schema.dump(role_objects)

    # serializing as JSON
    session.close()
    return jsonify(roles)
    
@app.route('/roles', methods=['POST'])
def add_role():
    # mount role object
    posted_role = RoleSchema(only=('name', 'prefix'))\
        .load(request.get_json())

    role = Role(**posted_role, created_by="System")

    # persist role
    session = Session()
    session.add(role)
    session.commit()

    # return created role
    new_role = RoleSchema().dump(role)
    session.close()
    return jsonify(new_role), 201

@app.route('/users')
def get_user():
    # fetching from the database
    session = Session()
    user_objects = session.query(User).all()

    # transforming into JSON-serializable objects
    schema = UserSchema(many=True)
    users = schema.dump(user_objects)

    # serializing as JSON
    session.close()
    return jsonify(users)
    
@app.route('/users', methods=['POST'])
def add_user():
    # mount user object
    posted_user = UserSchema(only=('name', 'lastname', 'code', 'phone', 'address', 'email', 'role_id'))\
        .load(request.get_json())

    user = User(**posted_user, created_by="System")

    # persist user
    session = Session()
    session.add(user)
    session.commit()

    # return created user
    new_user = UserSchema().dump(user)
    session.close()
    return jsonify(new_user), 201


@app.route('/models')
def get_model():
    # fetching from the database
    session = Session()
    model_objects = session.query(Model).all()

    # transforming into JSON-serializable objects
    schema = ModelSchema(many=True)
    models = schema.dump(model_objects)

    # serializing as JSON
    session.close()
    return jsonify(models)
    
@app.route('/models', methods=['POST'])
def add_model():
    # mount model object
    posted_model = ModelSchema(only=('name', 'description', 'file_name', 'file_path', 'user_id'))\
        .load(request.get_json())
    # fetching from the database
    session = Session()
    user_object = session.query(User).get(posted_model['user_id'])
    model = Model(**posted_model, created_by=f'{user_object.name} {user_object.lastname}')

    # persist model
    session.add(model)
    session.commit()

    # return created model
    new_model = ModelSchema().dump(model)
    session.close()
    return jsonify(new_model), 201

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'