from flask_restful import Resource


class  ApiView(Resource):
    def __init__(self, parser, db):
        self.parser = parser
        self.db = db
