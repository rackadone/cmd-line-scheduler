'''
StorageManager class

* This object handles all persistent file storage

'''

class StorageManager:
    def __init__(self, file_name="default.json"):
        self.file_name = file_name