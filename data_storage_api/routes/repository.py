from http import HTTPStatus
from flask import make_response, request, jsonify

from .base import ApiView


class  RepositoryResource(ApiView):
    
    def get(self, repository: str, object_id: str):
        
        obj = self.db.search_by_id(repository, object_id)
        if obj is None:
            return make_response({}, HTTPStatus.NOT_FOUND)
        json_response = jsonify(obj.decoded_data)

        return make_response(json_response, HTTPStatus.OK)
    
    def put(self, repository: str):
        
        json_data = request.get_json(force=True)        
        obj_id = self.db.add(repository, json_data)
        json_response = jsonify(oid=obj_id, size=request.content_length)
        
        response = make_response(json_response, HTTPStatus.CREATED)
        return response
    
    def delete(self, repository: str, object_id: str):
        
        obj = self.db.search_by_id(repository, object_id)
        if obj is None:
            return make_response({}, HTTPStatus.NOT_FOUND)
        if self.db.remove_by_id(repository, object_id):
            return make_response({},HTTPStatus.OK)
        return make_response({}, HTTPStatus.INTERNAL_SERVER_ERROR)
