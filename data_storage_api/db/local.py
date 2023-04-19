import base64
import json
from uuid import uuid4

from data_storage_api.utils import Singleton
from data_storage_api.dataclasses import RepositoryDataclass, ObjectDataclass


class MemoryDB(Singleton):
    
    __memory = {}
    
    def add_repository(self, repository: str):
        self.__memory[repository] = []
        return 
    
    def add(self, repository: str, data: str):
        if self.__memory.get(repository, None) is None:
            self.add_repository(repository=repository)
        b64_data = base64.b64encode(bytes(json.dumps(data), 'utf-8')).decode()
        obj = self.search_by_value(repository=repository, value=b64_data)
        if obj is None:
            object_id = str(uuid4())
            obj = ObjectDataclass(id=object_id, data=b64_data)
            self.__memory[repository].append(obj)
        
        return obj.id
    
    def get_objects(self):
        return self.__memory
    
    def search_by_id(self, repository: str, object_id: str):
        repository = self.__get_repository(repository=repository)
        if repository is None:
            return
        obj = self.__get_object_from_repository_by_id(repository=repository, object_id=object_id)
        
        return obj
    
    def search_by_value(self, repository: str, value: str):
        repository = self.__get_repository(repository=repository)
        if repository is None:
            return
        obj = self.__get_object_from_repository_by_value(repository=repository, value=value)
        
        return obj
    
    def remove_by_id(self, repository: str, object_id: str):
        repository = self.__get_repository(repository=repository)
        if repository is None:
            return
        obj = self.__remove_object_from_repository_by_id(repository=repository, object_id=object_id)
        
        return obj
    
    def __get_repository(self, repository: str):
        repo = self.__memory.get(repository, None)
        if repo is None:
            return
        return RepositoryDataclass(name=repository, data=repo)
    
    def __get_object_from_repository_by_id(self, repository: RepositoryDataclass, object_id: str):
        objects = [obj for obj in repository.data if obj.id == object_id]
        return objects.pop() if len(objects) else None
    
    def __get_object_from_repository_by_value(self, repository: RepositoryDataclass, value: str):
        objects = [obj for obj in repository.data if obj.data == value]
        return objects.pop() if len(objects) else None
    
    def __remove_object_from_repository_by_id(self, repository: RepositoryDataclass, object_id: str):
        new_objects = [obj for obj in repository.data if obj.id != object_id]
        self.__memory[repository.name] = new_objects
        return repository
