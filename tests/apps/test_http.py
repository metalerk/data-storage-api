from unittest import TestCase
from data_storage_api.apps.http import create_app
from data_storage_api.db import MemoryDB


class TestAPI(TestCase):
    
    def setUp(self) -> None:
        self.app = create_app()
        self.db = MemoryDB()
        return super().setUp()
    
    def test_add_repository(self):

        self.db.add_repository('north_america')
        self.db.add_repository('europe')
        self.db.add_repository('test3')
        
        self.assertIsNotNone(self.db.get_objects().get('north_america', None))
        self.assertIsNotNone(self.db.get_objects().get('europe', None))
        self.assertIsNotNone(self.db.get_objects().get('test3', None))
        
    def test_add_object(self):
        
        mx = {"code": "mx"}
        nl = {"code": "nl"}
        us = {"code": "us"}

        mx_id = self.db.add('north_america', mx)
        self.assertEqual(self.db.search_by_id('north_america', mx_id).decoded_data, mx)
        
        nl_id = self.db.add('europe', nl)
        self.assertEqual(self.db.search_by_id('europe', nl_id).decoded_data, nl)
        
        us_id = self.db.add('north_america', us)
        self.assertEqual(self.db.search_by_id('north_america', us_id).decoded_data, us)
