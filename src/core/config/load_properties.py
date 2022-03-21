"""
This file is used to create the handler for loading the system properties.
The properties will be loaded and passed on for use in entire project.
The properties are loaded only once for the entire project.
"""

# Importing required python libraries for processing
from jproperties import Properties


class LoadProperties:
    def __init__(self):
        print("This load_properties.py")
        self.configs = Properties()

    def fetch_properties(self):
        with open('', 'rb') as read_prop:
            self.configs.load(read_prop)

        prop_view = self.configs.items()
        print(type(prop_view))

        for item in prop_view:
            print(item)
