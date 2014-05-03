'''
StorageManager class

* This object handles all persistent file storage at a single file

'''

import json
import os

class StorageManager:
    def __init__(self, file_name="default.json"):
        """ Creates a specific storage file.
        """
        if not file_name:
            self.file_name = "schedules/default.json"
        else:
            self.file_name = "schedules/" + file_name
        if not os.path.isfile(self.file_name):
            fp = open(self.file_name, 'w+')
            # By default, the file is first initialized with
            # an empty dictionary
            json.dump({}, fp)
            fp.close()

    def get_json_object(self):
        """ Returns everything in json file as a dictionary
        """
        fp = open(self.file_name, 'r+')
        json_obj = json.loads(fp.read())
        fp.close()
        return json_obj

    def store_json_object(self, json_obj):
        """ Store object into file
        """
        fp = open(self.file_name, 'w+')
        json.dump(json_obj, fp)
        fp.close()