import random
import string

from flask import Flask
from flask_restful import Api, reqparse

from data_storage_api.routes import RepositoryResource
from data_storage_api.db import MemoryDB


def create_app():
    
    app = Flask(__name__)
    api = Api(app)

    app.config['SECRET_KEY'] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(50))

    db = MemoryDB()

    parser = reqparse.RequestParser()

    api.add_resource(
        RepositoryResource,
        '/data/<string:repository>/',
        '/data/<string:repository>/<string:object_id>/',
        resource_class_kwargs={'parser': parser, 'db': db}
    )
    
    parser.add_argument('repository', type=str)
    parser.add_argument('object_id', type=str)
    
    return app
