"""
This file is used to create the handler for loading the system properties.
The properties will be loaded and passed on for use in entire project.
The properties are loaded only once for the entire project.
"""

# Importing required python libraries for processing
from jproperties import Properties


class LoadProperties:
    """
    This is the class to load all the properties and make them available to the entire project.
    """
    def __init__(self, global_properties):
        """
        This method creates an object for the properties class.
        """
        self.configs = Properties()
        self.global_properties = global_properties
        self.file_path = self.global_properties['configurations']

    def fetch_properties(self):
        """
        This method opens up the properties file, reads the file and fetches all the parameters.
        """

        with open(self.file_path, 'rb') as file:
            self.configs.load(file)

        properties = self.configs.items()

        for item in properties:
            key = item[0]
            value = item[1].data
            self.global_properties[key] = value

        return self.global_properties
