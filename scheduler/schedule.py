import xml.etree.ElementTree as ET
import os

class Schedule:
    def __init__(self, year):
        self.file_name = "schedules/schedule_" + str(year) + ".xml"
        # If schedule subdirectory doesn't exist, create one.
        if not os.path.exists("schedules"):
            os.makedirs("schedules")
        # If 
        if (os.path.exists(self.file_name)):
            self.tree = ET.parse(self.file_name)
            self.root = self.tree.getroot()
        else: # Create empty XML tree
            self.root = ET.fromstring('<?xml version="1.0"?><data></data>')
            self.tree = ET.ElementTree()
            self.tree._setroot(self.root)

    def write_to_file(self):
        self.tree.write(self.file_name)

    # Example: ('January', 2, '12:00', 'Lunch', 'Lunch with Hyemin')
    def add_event(self, month, day, time, event):
        # Check if the month Exists
        if (self.root.find(month) is None):
            new_month = ET.Element(month)
            self.root.append(new_month)

        # Check if day exists

        # Create event element
        
    def getRootTag (self):
        return self.root.tag