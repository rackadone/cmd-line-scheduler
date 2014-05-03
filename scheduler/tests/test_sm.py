import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from utils.storage_manager import StorageManager

class TestStorageManager (unittest.TestCase):

    def tearDown(self):
        if os.path.isfile("schedules/test.json"):
            print "Deleting test.json"
            os.remove("schedules/test.json")

    def test_file_create(self):
        test_storage_manager = StorageManager("test.json")
        self.assertTrue(os.path.isfile("schedules/test.json"))
        os.remove("schedules/test.json")
        self.assertFalse(os.path.isfile("schedules/test.json"))

    def test_get_json_object(self):
        test_storage_manager = StorageManager("test.json")
        self.assertFalse(test_storage_manager.get_json_object())

    def test_store_json_object(self):
        test_object = {"abc" : "abc"}
        test_storage_manager = StorageManager("test.json")
        test_storage_manager.store_json_object(test_object)
        stored_object = test_storage_manager.get_json_object()
        self.assertEqual(test_object, stored_object)

if __name__ == '__main__' :
    unittest.main()